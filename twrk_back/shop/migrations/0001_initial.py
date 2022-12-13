# Generated by Django 4.1.4 on 2022-12-13 09:16

import django.core.validators
from django.db import migrations, models
import shop.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('article', models.CharField(max_length=255, verbose_name='артикул')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=14, verbose_name='цена')),
                ('status', models.CharField(choices=[('IN_STOCK', 'В наличии'), ('ON_ORDER', 'Под заказ'), ('RECEIPT_EXPECTED', 'Ожидается поступление'), ('NOT_AVAILABLE', 'Нет в наличии'), ('NOT_PRODUCED', 'Не производится')], max_length=21, verbose_name='статус')),
                ('image', shop.fields.WEBPField(upload_to='images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'webp'])])),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'ordering': ('title',),
            },
        ),
    ]