from django.urls import path, register_converter
from app.views import file_list, file_content

from . import path_converters

register_converter(path_converters.DateConverter, 'date')

urlpatterns = [
    path('', file_list, name='file_list'),
    path('<date:filter_date>/', file_list, name='file_list'),
    path('file_content/<str:file_name>/', file_content, name='file_content'),
]
