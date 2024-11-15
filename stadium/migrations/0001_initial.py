# Generated by Django 5.1.2 on 2024-11-05 18:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryOfService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название услуги')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='TypeOfService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Тип услуги')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение услуги')),
                ('description', models.TextField(verbose_name='Описание услуги')),
                ('best', models.BooleanField(default=False, verbose_name='Продвигаемое')),
                ('category_of_service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stadium.categoryofservice', verbose_name='Категория услуги')),
            ],
            options={
                'verbose_name': 'Тип услуги',
                'verbose_name_plural': 'Тип услуг',
            },
        ),
        migrations.CreateModel(
            name='TypeOfSubService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Тип подсервиса')),
                ('unit', models.CharField(max_length=256, verbose_name='Единица измерения')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость')),
                ('type_of_service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stadium.typeofservice', verbose_name='Тип услуги')),
            ],
            options={
                'verbose_name': 'Тип услуги',
                'verbose_name_plural': 'Тип услуг',
            },
        ),
    ]
