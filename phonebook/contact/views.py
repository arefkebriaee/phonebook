from django.shortcuts import render, get_object_or_404
from .models import Contact


def show_all(request):
    contact_list = Contact.objects.all()
    return render(request, 'contact/all-contacts.html', {'contacts': contact_list})


def one_contact(request, id, name):
    contact = get_object_or_404(Contact, id=id, contact_name=name)
    return render(request, "contact/detail-contact.html", {'contact': contact})
