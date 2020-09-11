from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'(?P<url>[0-9]+/)', views.good_page, name='good_page')
]