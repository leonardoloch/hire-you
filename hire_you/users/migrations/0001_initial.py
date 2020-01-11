# Generated by Django 2.2.5 on 2020-01-11 14:52

from django.db import migrations, models
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=32, verbose_name='first name')),
                ('last_name', models.CharField(max_length=64, verbose_name='last name')),
                ('date_of_birth', models.DateField(null=True, verbose_name='date of birth')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email address')),
                ('email_confirmed', models.BooleanField(default=False, verbose_name='email confirmed')),
                ('phone_number', models.CharField(max_length=16, null=True, verbose_name='phone number')),
                ('terms_accepted', models.BooleanField(default=False, verbose_name='terms accepted')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]