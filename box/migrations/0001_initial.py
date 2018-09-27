# Generated by Django 2.0.3 on 2018-09-26 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('description', models.CharField(max_length=250, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Chocolate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=250, null=True, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
            ],
        ),
        migrations.CreateModel(
            name='ChocolateType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
            ],
        ),
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
            ],
        ),
        migrations.AddField(
            model_name='chocolate',
            name='chocolate_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='box.ChocolateType', verbose_name='Chocolate type'),
        ),
        migrations.AddField(
            model_name='chocolate',
            name='fruit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='box.Fruit', verbose_name='Fruit'),
        ),
        migrations.AddField(
            model_name='box',
            name='chocolate',
            field=models.ManyToManyField(blank=True, to='box.Chocolate'),
        ),
    ]
