# Generated by Django 3.1.1 on 2020-09-20 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200916_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor_feedback',
            name='plasma_bank',
            field=models.CharField(max_length=20),
        ),
    ]
