# Generated by Django 4.1.6 on 2023-02-16 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0003_alter_occasion_description_alter_occasion_occasion'),
    ]

    operations = [
        migrations.CreateModel(
            name='itemtype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemtype', models.CharField(max_length=150, null=True)),
                ('description', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='occasion',
            name='category',
        ),
        migrations.AddField(
            model_name='occasion',
            name='itemtype',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
