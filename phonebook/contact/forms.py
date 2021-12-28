from django import forms
from django.db.models import fields
from .models import Contact, Mobile, Phone, Fax, Social, Email, Address


class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=50, required=True)
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    # image = forms.FileField(required=False)
    birthday = forms.DateField(required=False)
    real_person = forms.CharField(max_length=20, required=False)


class EditContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('contact_name', 'first_name',
                  'last_name', 'birthday', 'real_person')


class MobileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MobileForm, self).__init__(*args, **kwargs)
        self.fields['mobile_number'].required = False

    class Meta:
        model = Mobile
        fields = ('mobile_number',)


class EditMobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ('mobile_number',)


class PhoneForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PhoneForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].required = False

    class Meta:
        model = Phone
        fields = ('phone_number',)


class FaxForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FaxForm, self).__init__(*args, **kwargs)
        self.fields['fax_number'].required = False

    class Meta:
        model = Fax
        fields = ('fax_number',)


class SocialForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SocialForm, self).__init__(*args, **kwargs)
        self.fields['social_name'].required = False
        self.fields['social_address'].required = False

    class Meta:
        model = Social
        fields = ('social_name', 'social_address')


class EmailForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False

    class Meta:
        model = Email
        fields = ('email',)


class AddressForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        self.fields['address'].required = False

    class Meta:
        model = Address
        fields = ('address',)
