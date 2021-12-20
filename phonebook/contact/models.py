from django.db import models
from django.urls import reverse
# Create your models here.


class Contact(models.Model):
    person_status = (('real person', 'Real person'),
                     ('legal person', 'Legal person'))
    contact_name = models.CharField(max_length=50, blank=False)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    image = models.ImageField(
        upload_to='images/', blank=True)
    real_person = models.CharField(choices=person_status, max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_name

    def get_absolute_url(self):
        return reverse("contact:detail", args=[self.id, self.contact_name])
