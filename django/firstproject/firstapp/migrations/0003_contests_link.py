# Generated by Django 2.1.7 on 2019-04-07 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20190309_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='contests',
            name='link',
            field=models.CharField(default='DEFAULT VALUE', max_length=200),
        ),
    ]