# Generated by Django 4.0 on 2021-12-24 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0013_remove_person_car_remove_contact_image_delete_car_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mobile',
            old_name='number',
            new_name='mobile_number',
        ),
    ]