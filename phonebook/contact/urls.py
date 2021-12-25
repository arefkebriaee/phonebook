from os import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'contact'
urlpatterns = [
    path('', views.home, name='home'),
    path("all/", views.show_all, name='all'),
    path("<int:id>/<str:name>/", views.one_contact, name='detail'),
    path("create/", views.create_contact, name='contact-create'),
    path("edit/<int:id>/<str:name>/", views.edit_contact, name='edit'),
]
