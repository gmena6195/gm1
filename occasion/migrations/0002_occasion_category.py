# Generated by Django 4.1.6 on 2023-02-16 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='occasion',
            name='category',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
