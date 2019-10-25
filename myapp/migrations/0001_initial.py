# Generated by Django 2.2 on 2019-10-23 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(max_length=500)),
                ('created', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Searches',
            },
        ),
    ]