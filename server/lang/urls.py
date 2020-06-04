from django.urls import path

from . import views

urlpatterns = [
    path('languages/', views.languages, name='languages'),
    path('', views.translate, name='translate'),
    path('json/', views.translateJsonFile, name='translateJsonFile'),
]
