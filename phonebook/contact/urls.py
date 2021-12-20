from os import name
from django.urls import path
from . import views

app_name = 'contact'
urlpatterns = [
    path("all/", views.show_all, name='all'),
    path("<int:id>/<str:name>/", views.one_contact, name='detail')
]
