# Generated by Django 3.0.6 on 2020-09-11 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital_feedback',
            name='plasma_bank',
            field=models.CharField(max_length=20),
        ),
    ]
