from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.Scraping, name='index'),
    path('download_list/', views.Download_List, name='download_list'),
]