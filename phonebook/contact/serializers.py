from django.db.models import fields
from rest_framework import serializers
from .models import Contact, Mobile, Phone, Fax, Social, Email, Address


class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = ('owner', 'number')


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('owner', 'number')


class FaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fax
        fields = ('owner', 'number')


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ('owner', 'name', 'address')


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ('owner', 'email')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('owner', 'address')


class ContactSerializer(serializers.ModelSerializer):
    mobile = MobileSerializer(many=True)
    phone = PhoneSerializer(many=True)
    fax = FaxSerializer(many=True)
    social = SocialSerializer(many=True)
    email = EmailSerializer(many=True)
    address = AddressSerializer(many=True)

    class Meta:
        model = Contact
        fields = ('contact_name', 'first_name', 'last_name', 'image',
                  'birthday', 'creator', 'real_person', 'mobile', 'phone',
                  'fax', 'social', 'email', 'address')
