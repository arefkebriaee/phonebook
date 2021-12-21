from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    person_status = (('real person', 'Real person'),
                     ('legal person', 'Legal person'))

    contact_name = models.CharField(max_length=50, blank=False)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    image = models.ImageField(
        upload_to='images/', blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    real_person = models.CharField(choices=person_status, max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_name

    def get_absolute_url(self):
        return reverse("contact:detail", args=[self.id, self.contact_name])


class Mobile(models.Model):
    owner = models.ForeignKey(
        Contact, on_delete=models.CASCADE, related_name='mobile')
    number = PhoneNumberField(blank=False)

    def __str__(self) -> str:
        return str(self.number)


class Phone(models.Model):
    owner = models.ForeignKey(
        Contact, on_delete=models.CASCADE, related_name='phone')
    number = PhoneNumberField(blank=False)

    def __str__(self) -> str:
        return str(self.number)


class Fax(models.Model):
    owner = models.ForeignKey(
        Contact, on_delete=models.CASCADE, related_name='fax')
    number = PhoneNumberField(blank=False)

    def __str__(self) -> str:
        return str(self.number)
