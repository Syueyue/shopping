# Generated by Django 2.0.1 on 2018-01-20 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ta_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uemil',
            field=models.EmailField(default='', max_length=30),
        ),
    ]
