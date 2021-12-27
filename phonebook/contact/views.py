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
from django.views.decorators.csrf import csrf_exempt


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


# @api_view(['GET', 'POST'])
@csrf_exempt
def edit_contact(request, id, name, section=None, data=None):
    contact = Contact.objects.get(
        id=id, contact_name=name, creator=request.user)
    if request.method == 'POST':
        if section == 'personal':
            contact_form = EditContactForm(request.POST)
            if contact_form.is_valid():
                # edited_contact = contact_form.save(commit=False)
                Contact.objects.filter(
                    id=id, contact_name=name, creator=request.user).update(
                    id=contact.id,
                    contact_name=contact_form.cleaned_data['contact_name'],
                    first_name=contact_form.cleaned_data['first_name'],                                                                      last_name=contact_form.cleaned_data['last_name'],
                    birthday=contact_form.cleaned_data['birthday'],
                    creator=request.user,
                    real_person=contact_form.cleaned_data['real_person'],
                    created=contact.created)
        elif section == 'mobile':
            mobile_form = EditMobileForm(request.POST)
            if mobile_form.is_valid():
                mobile = Mobile.objects.filter(owner=id, mobile_number=data).update(
                    mobile_number=mobile_form.cleaned_data['mobile_number'])
        elif section == 'phone':
            phone_form = PhoneForm(request.POST)
            if phone_form.is_valid():
                phone = Phone.objects.filter(owner=id, phone_number=data).update(
                    phone_number=phone_form.cleaned_data['phone_number'])
        elif section == 'fax':
            fax_form = FaxForm(request.POST)
            if fax_form.is_valid():
                fax = Fax.objects.filter(owner=id, fax_number=data).update(
                    fax_number=fax_form.cleaned_data['fax_number'])
        elif section == 'social':
            social_form = SocialForm(request.POST)
            if social_form.is_valid():
                social = Social.objects.filter(owner=id, social_name=data).update(
                    social_name=social_form.cleaned_data['social_name'],
                    social_address=social_form.cleaned_data['social_address'])
        elif section == 'email':
            email_form = EmailForm(request.POST)
            if email_form.is_valid():
                email = Email.objects.filter(owner=id, email=data).update(
                    email=email_form.cleaned_data['email'])
        elif section == 'address':
            address_form = AddressForm(request.POST)
            if address_form.is_valid():
                address = Address.objects.filter(owner=id, address=data).update(
                    address=address_form.cleaned_data['address'])
        return redirect('contact:detail', contact.id, contact.contact_name)
    else:
        if section == 'personal':
            form = EditContactForm(instance=contact)
        elif section == 'mobile':
            mobile = Mobile.objects.filter(owner=id, mobile_number=data)
            form = EditMobileForm(instance=mobile[0])
        elif section == 'phone':
            phone = Phone.objects.filter(owner=id, phone_number=data)
            form = PhoneForm(instance=phone[0])
        elif section == 'fax':
            fax = Fax.objects.filter(owner=id, fax_number=data)
            form = FaxForm(instance=fax[0])
        elif section == 'social':
            social = Social.objects.filter(owner=id, social_name=data)
            form = SocialForm(instance=social[0])
        elif section == 'email':
            email = Email.objects.filter(owner=id, email=data)
            form = EmailForm(instance=email[0])
        elif section == 'address':
            address = Address.objects.filter(owner=id, address=data)
            form = AddressForm(instance=address[0])
        return render(request, 'contact/edit-contact.html', {'form': form})


def delete(request, id, name, section=None, data=None):
    contact = Contact.objects.get(id=id, contact_name=name)
    if section == 'personal':
        contact.delete()
        return redirect('contact:all')
    elif section == 'mobile':
        contact.mobile.get(mobile_number=data).delete()
    elif section == 'phone':
        contact.phone.get(phone_number=data).delete()
    elif section == 'fax':
        contact.fax.get(fax_number=data).delete()
    elif section == 'social':
        contact.social.get(social_name=data).delete()
    elif section == 'email':
        contact.email.get(email=data).delete()
    elif section == 'address':
        contact.address.get(address=data).delete()
    return redirect('contact:detail', contact.id, contact.contact_name)


@csrf_exempt
def add_number(request, id, name, section=None):
    contact = Contact.objects.get(id=id, contact_name=name)
    if request.method == 'POST':
        if section == 'mobile':
            form = MobileForm(request.POST)
        elif section == 'phone':
            form = PhoneForm(request.POST)
        elif section == 'fax':
            form = FaxForm(request.POST)
        elif section == 'social':
            form = SocialForm(request.POST)
        elif section == 'email':
            form = EmailForm(request.POST)
        elif section == 'address':
            form = AddressForm(request.POST)
        if form.is_valid():
            new_obj = form.save(commit=False)
            new_obj.owner = contact
            new_obj.save()
        return redirect('contact:detail', contact.id, contact.contact_name)
    else:
        if section == 'mobile':
            form = MobileForm()
        elif section == 'phone':
            form = PhoneForm()
        elif section == 'fax':
            form = FaxForm()
        elif section == 'social':
            form = SocialForm()
        elif section == 'email':
            form = EmailForm()
        elif section == 'address':
            form = AddressForm()
        return render(request, 'contact/add-number.html', {'form': form})
