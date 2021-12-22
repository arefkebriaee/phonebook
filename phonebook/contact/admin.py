from django.contrib import admin
from .models import Contact, Mobile, Phone, Fax, Social, Email
# Register your models here.

admin.site.register(Contact)
admin.site.register(Mobile)
admin.site.register(Phone)
admin.site.register(Fax)
admin.site.register(Social)
admin.site.register(Email)
