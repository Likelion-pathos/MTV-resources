# Generated by Django 5.0.6 on 2024-06-24 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookinfos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default='', verbose_name='관람팁'),
        ),
    ]
