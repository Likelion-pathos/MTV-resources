# Generated by Django 5.0.6 on 2024-06-25 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=128, verbose_name='제목'),
        ),
    ]
