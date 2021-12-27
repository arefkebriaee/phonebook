from django.db import models
from django.db.models.fields import DateField, EmailField, URLField
from django.urls import reverse
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    person_status = (('real person', 'Real person'),
                     ('legal person', 'Legal person'))

    contact_name = models.CharField(max_length=50, blank=False)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    # image = models.ImageField(
    #     upload_to='images/', blank=True, default="/static/public/images/icons8-person-64.png")
    birthday = models.DateField(blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    real_person = models.CharField(choices=person_status, max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_name

    def get_absolute_url(self):
        return reverse("contact:detail", args=[self.id, self.contact_name])

    class Meta:
        ordering = ['contact_name']


class Mobile(models.Model):
    owner = models.ForeignKey(
        Contact, on_delete=models.CASCADE, related_name='mobile')
    mobile_number = PhoneNumberField(blank=False)

    def __str__(self):
        return str(self.mobile_number)


class Phone(models.Model):
    owner = models.ForeignKey(
        Contact, on_delete=models.CASCADE, related_name='phone')
    phone_number = PhoneNumberField(blank=False)

    def __str__(self):
        return str(self.phone_number)


class Fax(models.Model):
    owner = models.ForeignKey(
        Contact, on_delete=models.CASCADE, related_name='fax')
    fax_number = PhoneNumberField(blank=False)

    def __str__(self):
        return str(self.fax_number)


class Social(models.Model):
    social_media = (
        ('instagram', 'Instagram'),
        ('linkedin', 'Linkedin'),
        ('twitter', 'Twitter'),
    )
    owner = models.ForeignKey(
        Contact, on_delete=models.CASCADE, related_name='social')
    social_name = models.CharField(choices=social_media,
                                   max_length=50, default='linkedin')
    social_address = URLField()

    def __str__(self):
        return str(self.social_name)


class Email(models.Model):
    owner = models.ForeignKey(
        Contact, on_delete=models.CASCADE, related_name='email')
    email = EmailField()

    def __str__(self):
        return str(self.email)


class Address(models.Model):
    owner = models.ForeignKey(
        Contact, on_delete=models.CASCADE, related_name='address')
    address = models.TextField()
