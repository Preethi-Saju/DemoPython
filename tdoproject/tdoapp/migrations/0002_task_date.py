# Generated by Django 4.2.10 on 2024-02-21 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tdoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1995-02-25'),
            preserve_default=False,
        ),
    ]
