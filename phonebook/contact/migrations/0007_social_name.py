# Generated by Django 4.0 on 2021-12-21 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='social',
            name='name',
            field=models.CharField(choices=[('instagram', 'Instagram'), ('linkedin', 'Linkedin'), ('twitter', 'Twitter')], default='linkedin', max_length=50),
        ),
    ]