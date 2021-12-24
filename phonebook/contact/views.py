from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from rest_framework.settings import import_from_string
from .models import Contact, Mobile, Phone, Fax, Social, Email, Address
from .serializers import ContactSerializer
from rest_framework.decorators import api_view
from .forms import ContactForm
from django.contrib import messages
from django.views.decorators import csrf
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
    header_info = dict(itertools.islice(serializer.data.items(), 6))
    body_info = dict(itertools.islice(serializer.data.items(), 6, None))
    return render(request, "contact/detail-contact.html",
                  {'header': header_info, 'body': body_info})


@api_view(['GET', 'POST'])
def create_contact(request):
    if request.method == 'POST':
        print("@@@&&&\n", request.FILES)
        print("@@@&&&\n", request.data)
        # form = ContactForm(request.POST, request.FILES)
        serializer = ContactSerializer(data=request.data)
        print("@@@&&&\n", serializer)
        if serializer.is_valid():
            # print("##########\n", form.cleaned_data)
            # if serializer.validated_data['real_person']:
            real_person_status = 'Real person'
            # else:
            # real_person_status = 'Legal person'
            print("$$$$\n", serializer.validated_data)
            Contact(contact_name=serializer.validated_data['contact_name'],
                    first_name=serializer.validated_data['first_name'],
                    last_name=serializer.validated_data['last_name'],
                    # image=serializer.validated_data['image'],
                    birthday=serializer.validated_data['birthday'],
                    creator=request.user,
                    real_person=real_person_status).save()
            messages.success(request, "contact create successfuly")
            return redirect("contact:all")
        else:
            messages.warning(request, serializer.errors)
            return redirect("contact:contact-create")

    form = ContactForm()
    return render(request, 'contact/test.html', {'form': form})
