from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название продукта')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name= 'Стоимость')
    image = models.ImageField(blank=True,null=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} --- {self.price}'
