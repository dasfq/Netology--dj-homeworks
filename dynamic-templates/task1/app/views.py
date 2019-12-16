from django.shortcuts import render
import csv


def inflation_view(request=None):
    template_name = 'inflation.html'
    data = []
    with open('inflation_russia.csv', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            for cell in row:
                try:
                    cell = float(cell)
                except:
                    cell = cell
            data.append(row)
    context = {
        'data': data
    }

    return render(request, template_name, context)