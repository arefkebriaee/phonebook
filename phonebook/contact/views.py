from django.forms.formsets import formset_factory
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from rest_framework import serializers
from rest_framework.settings import import_from_string
from .models import Contact, Mobile, Phone, Fax, Social, Email, Address
from .serializers import ContactSerializer, ContactCreateSerializer, MobileSerializer, PhoneSerializer, FaxSerializer, SocialSerializer, EmailSerializer, AddressSerializer
from rest_framework.decorators import api_view
from .forms import ContactForm, EditContactForm, MobileForm, EditMobileForm, PhoneForm, FaxForm, SocialForm, EmailForm, AddressForm
from django.contrib import messages
from django.forms import formset_factory
import itertools


def home(request):
    return render(request, 'contact/home.html')


def show_all(request):
    contact_list = Contact.objects.all()
    return render(request, 'contact/all-contacts.html', {'contacts': contact_list})


@api_view()
def one_contact(request, id, name):
    contact = get_object_or_404(Contact, id=id, contact_name=name)
    serializer = ContactSerializer(contact)
    header_info = dict(itertools.islice(serializer.data.items(), 7))
    body_info = dict(itertools.islice(serializer.data.items(), 7, None))
    return render(request, "contact/detail-contact.html",
                  {'header': header_info, 'body': body_info})


@api_view(['GET', 'POST'])
def create_contact(request):
    if request.method == 'POST':
        print(request.data)
        serializer = ContactCreateSerializer(data=request.data)
        if serializer.is_valid():
            real_person_status = 'Real person'
            Contact(contact_name=serializer.validated_data['contact_name'],
                    first_name=serializer.validated_data['first_name'],
                    last_name=serializer.validated_data['last_name'],
                    # image=serializer.validated_data['image'],
                    birthday=serializer.validated_data['birthday'],
                    creator=request.user,
                    real_person=real_person_status).save()
            person = Contact.objects.last().id
            if request.data['mobile_number']:
                mobile_serializer = MobileSerializer(
                    data={'owner': person, 'mobile_number': request.data['mobile_number']})
                if mobile_serializer.is_valid():
                    Mobile(owner=mobile_serializer.validated_data['owner'],
                           mobile_number=mobile_serializer.validated_data['mobile_number']).save()
            if request.data['phone_number']:
                phone_serializer = PhoneSerializer(data={
                    'owner': person, 'phone_number': request.data['phone_number']})
                if phone_serializer.is_valid():
                    Phone(owner=phone_serializer.validated_data['owner'],
                          phone_number=phone_serializer.validated_data['phone_number']).save()
            if request.data['fax_number']:
                fax_serializer = FaxSerializer(data={
                    'owner': person, 'fax_number': request.data['fax_number']})
                if fax_serializer.is_valid():
                    Fax(owner=fax_serializer.validated_data['owner'],
                        fax_number=fax_serializer.validated_data['fax_number']).save()
            if request.data['social_address']:
                social_serializer = SocialSerializer(data={
                    'owner': person, 'social_name': request.data['social_name'],
                    'social_address': request.data['social_address']})
                if social_serializer.is_valid():
                    Social(owner=social_serializer.validated_data['owner'],
                           social_name=social_serializer.validated_data['social_name'],
                           social_address=social_serializer.validated_data['social_address']).save()
            if request.data['email']:
                email_serializer = EmailSerializer(data={
                    'owner': person, 'email': request.data['email']})
                if email_serializer.is_valid():
                    Email(owner=email_serializer.validated_data['owner'],
                          email=email_serializer.validated_data['email']).save()
            if request.data['address']:
                address_serializer = AddressSerializer(data={
                    'owner': person, 'address': request.data['address']})
                if address_serializer.is_valid():
                    Address(owner=address_serializer.validated_data['owner'],
                            address=address_serializer.validated_data['address']).save()
            messages.success(request, "contact create successfuly")
            return redirect("contact:all")
        else:
            messages.warning(request, serializer.errors)
            return redirect("contact:contact-create")

    # form = ContactForm()
    contact_form = ContactForm()
    mobile_form = MobileForm()
    phone_form = PhoneForm()
    fax_form = FaxForm()
    social_form = SocialForm()
    email_form = EmailForm()
    address_form = AddressForm()
    return render(request, 'contact/create-contact.html', {'contact_form': contact_form,
                                                           'mobile_form': mobile_form, 'phone_form': phone_form, 'fax_form': fax_form,
                                                           'social_form': social_form, 'email_form': email_form, 'address_form': address_form})


@api_view(['GET', 'PUT'])
def edit_contact(request, id, name):
    contact = Contact.objects.get(
        id=id, contact_name=name, creator=request.user)
    print("&&&&&&&&&&\n", contact)
    if request.method == 'PUT':
        pass
    else:
        mobile = Mobile.objects.filter(owner=id)
        print(mobile)
        contact_form = EditContactForm(instance=contact)
        # mobile_form = EditMobileForm(instance=mobile)
        # phone_form = PhoneForm(instance=contact)
        # fax_form = FaxForm(instance=contact)
        # social_form = SocialForm(instance=contact)
        # email_form = EmailForm(instance=contact)
        # address_form = AddressForm(instance=contact)
        return render(request, 'contact/edit-contact.html',
                      {'contact_form': contact_form})
