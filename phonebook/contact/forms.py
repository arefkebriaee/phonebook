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


class MobileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(MobileForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['mobile_number'].required = False

    class Meta:
        model = Mobile
        fields = ('mobile_number',)


class PhoneForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(PhoneForm, self).__init__(*args, **kwargs)
    #     self.fields['phone_number'].required = False

    class Meta:
        model = Phone
        fields = ('phone_number',)


class FaxForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(FaxForm, self).__init__(*args, **kwargs)
    #     self.fields['fax_number'].required = False

    class Meta:
        model = Fax
        fields = ('fax_number',)


class SocialForm(forms.ModelForm):
    class Meta:
        model = Social
        fields = ('social_name', 'social_address')


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('email',)


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('address',)
