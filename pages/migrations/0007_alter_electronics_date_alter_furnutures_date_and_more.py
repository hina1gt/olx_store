# Generated by Django 4.2.2 on 2023-08-09 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_clothes_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electronics',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='furnutures',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='households',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='sports',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
