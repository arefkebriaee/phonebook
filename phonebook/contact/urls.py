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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
