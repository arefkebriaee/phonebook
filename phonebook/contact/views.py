from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.settings import import_from_string
from .models import Contact, Mobile, Phone, Fax, Social, Email, Address
from .serializers import ContactSerializer
from rest_framework.decorators import api_view


def home(request):
    return render(request, 'contact/home.html')


def show_all(request):
    contact_list = Contact.objects.all()
    return render(request, 'contact/all-contacts.html', {'contacts': contact_list})


@api_view()
def one_contact(request, id, name):
    contact = get_object_or_404(Contact, id=id, contact_name=name)
    serializer = ContactSerializer(contact)
    return render(request, "contact/detail-contact.html", {'contact': serializer.data})
