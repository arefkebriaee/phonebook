from django.db import models
from django.db.models import fields
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from rest_framework import serializers
from .models import Contact, Mobile, Phone, Fax, Social, Email, Address
from drf_extra_fields.fields import Base64ImageField

# class Base64ImageField(serializers.ImageField):
#     """
#     A Django REST framework field for handling image-uploads through raw post data.
#     It uses base64 for encoding and decoding the contents of the file.

#     Heavily based on
#     https://github.com/tomchristie/django-rest-framework/pull/1268

#     Updated for Django REST framework 3.
#     """

#     def to_internal_value(self, data):
#         from django.core.files.base import ContentFile
#         import base64
#         from django.utils import six
#         import uuid

#         # Check if this is a base64 string
#         if isinstance(data, six.string_types):
#             # Check if the base64 string is in the "data:" format
#             if 'data:' in data and ';base64,' in data:
#                 # Break out the header from the base64 content
#                 header, data = data.split(';base64,')

#             # Try to decode the file. Return validation error if it fails.
#             try:
#                 decoded_file = base64.b64decode(data)
#             except TypeError:
#                 self.fail('invalid_image')

#             # Generate file name:
#             # 12 characters are more than enough.
#             file_name = str(uuid.uuid4())[:12]
#             # Get the file name extension:
#             file_extension = self.get_file_extension(file_name, decoded_file)

#             complete_file_name = "%s.%s" % (file_name, file_extension, )

#             data = ContentFile(decoded_file, name=complete_file_name)

#         return super(Base64ImageField, self).to_internal_value(data)

#     def get_file_extension(self, file_name, decoded_file):
#         import imghdr

#         extension = imghdr.what(file_name, decoded_file)
#         extension = "jpg" if extension == "jpeg" else extension

#         return extension


class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = ('owner', 'mobile_number')


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('owner', 'phone_number')


class FaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fax
        fields = ('owner', 'fax_number')


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ('owner', 'social_name', 'social_address')


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
    # image = Base64ImageField(
    #     max_length=None, use_url=True,
    # )

    class Meta:
        model = Contact
        fields = ('contact_name', 'first_name', 'last_name',
                  'birthday', 'creator', 'real_person', 'mobile', 'phone',
                  'fax', 'social', 'email', 'address')
        # fields = ('contact_name', 'first_name', 'last_name',
        #           'birthday', 'creator', 'real_person', 'mobile')


class ContactCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'contact_name', 'first_name', 'last_name',
                  'birthday', 'creator', 'real_person')
