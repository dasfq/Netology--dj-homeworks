import datetime, os, time

from django.shortcuts import render
from .settings import FILES_PATH
from dateutil import parser

def file_list(request, filter_date = None):
    template_name = 'index.html'
    files_list = os.listdir(FILES_PATH)
    context = {
        'files': [],
        'date': None
    }
    new_date = None

    if filter_date:
        year = int(filter_date.split('-')[0])
        month = int(filter_date.split('-')[1])
        day = int(filter_date.split('-')[2])
        new_date = datetime.date(year, month, day)
        context['date'] = new_date

    for f in files_list:
        file_path = os.path.join(FILES_PATH, f)
        file_stat = os.stat(path=FILES_PATH)
        file_info = {}
        file_info['name'] = f
        file_info['ctime'] = parser.parse(time.ctime(file_stat.st_ctime))
        file_info['mtime'] = parser.parse(time.ctime(file_stat.st_mtime))
        if not new_date:
            context['files'].append(file_info)
        elif new_date and new_date == file_info['ctime'].date():
            context['files'].append(file_info)
    return render(request, template_name, context)


def file_content(request, file_name):
    files_path = FILES_PATH
    file_path = os.path.join(files_path, file_name)
    if os.path.exists(file_path):
        with open(file_path) as file:
            content = file.read()
    else:
        content = 'Alarm! There is no file with entered name'
    return render(
        request,
        'file_content.html',
        context={'file_name': file_name,
                 'file_content': content}
    )
