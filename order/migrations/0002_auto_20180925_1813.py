# Generated by Django 2.0.3 on 2018-09-25 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='box',
            name='chocolate',
        ),
        migrations.RemoveField(
            model_name='chocolate',
            name='chocolate_type',
        ),
        migrations.RemoveField(
            model_name='chocolate',
            name='fruit',
        ),
        migrations.DeleteModel(
            name='Box',
        ),
        migrations.DeleteModel(
            name='Chocolate',
        ),
    ]
