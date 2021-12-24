from django import forms
from django.db.models import fields
from .models import Contact, Mobile


class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=50, required=True)
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    # image = forms.FileField(required=False)
    birthday = forms.DateField(required=False)
    real_person = forms.BooleanField(required=False)


class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ('number',)


class ContactCreateForm(forms.ModelForm):
    mobile = MobileForm()

    class Meta:
        model = Contact
        fields = ('contact_name', 'first_name', 'last_name',
                  'birthday', 'creator', 'real_person')
