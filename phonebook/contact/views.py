from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Contact, Mobile


def home(request):
    return render(request, 'contact/home.html')


def show_all(request):
    contact_list = Contact.objects.all()
    return render(request, 'contact/all-contacts.html', {'contacts': contact_list})


def one_contact(request, id, name):
    contact = get_object_or_404(Contact, id=id, contact_name=name)
    mobiles = get_list_or_404(Mobile, owner=id)
    return render(request, "contact/detail-contact.html", {'contact': contact, 'mobiles': mobiles})
