# Generated by Django 2.0.1 on 2018-02-02 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ta_goods', '0002_auto_20180202_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodinfo',
            name='gtype',
            field=models.ForeignKey(on_delete=None, to='ta_goods.TypeInfo'),
        ),
        migrations.AlterField(
            model_name='goodinfo',
            name='gunit',
            field=models.CharField(default='500', max_length=20),
        ),
    ]
