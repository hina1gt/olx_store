# Generated by Django 4.2.2 on 2023-08-09 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_households'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
