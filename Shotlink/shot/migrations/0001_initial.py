# Generated by Django 3.2.6 on 2021-08-27 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lien', models.CharField(max_length=10000)),
                ('idd', models.CharField(max_length=10)),
            ],
        ),
    ]
