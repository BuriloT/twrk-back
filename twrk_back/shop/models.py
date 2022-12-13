from django.core.validators import FileExtensionValidator
from django.db import models

from .fields import WEBPField
from twrk_back.settings import ALLOWED_EXTENSIONS


def product_directory_path(instance, filename):
    new_filename = filename.split('.')[:-1]
    return f'images/product_{new_filename}.webp'


class Product(models.Model):

    class Status(models.TextChoices):
        IN_STOCK = 'В наличии', 'В наличии'
        ON_ORDER = 'Под заказ', 'Под заказ'
        RECEIPT_EXPECTED = 'Ожидается поступление', 'Ожидается поступление'
        NOT_AVAILABLE = 'Нет в наличии', 'Нет в наличии'
        NOT_PRODUCED = 'Не производится', 'Не производится'

    title = models.CharField('название', max_length=255, null=False)
    article = models.CharField('артикул', max_length=255, null=False)
    cost = models.DecimalField('цена', max_digits=14, decimal_places=2)
    status = models.CharField('статус', max_length=21,
                              choices=Status.choices, default=Status.IN_STOCK)
    image = WEBPField(upload_to=product_directory_path, validators=[
        FileExtensionValidator(allowed_extensions=ALLOWED_EXTENSIONS)])

    class Meta:
        ordering = ('title',)
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return self.title
