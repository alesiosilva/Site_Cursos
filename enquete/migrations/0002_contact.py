# Generated by Django 3.2.8 on 2021-11-05 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquete', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('msg', models.TextField()),
            ],
        ),
    ]
