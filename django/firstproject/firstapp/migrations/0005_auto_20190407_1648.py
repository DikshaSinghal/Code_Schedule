# Generated by Django 2.1.7 on 2019-04-07 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20190407_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contests',
            name='link',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
