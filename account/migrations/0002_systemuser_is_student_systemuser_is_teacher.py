# Generated by Django 5.0.6 on 2024-12-18 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemuser',
            name='is_student',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='systemuser',
            name='is_teacher',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]