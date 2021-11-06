# Generated by Django 3.2.8 on 2021-11-05 23:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('enquete', '0004_contact_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='data',
        ),
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='data contato'),
        ),
    ]
