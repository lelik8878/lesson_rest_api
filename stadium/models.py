from django.db import models

class CategoryOfService(models.Model):
    """Model describes list of services"""
    title = models.CharField(max_length=256, verbose_name='Название услуги', unique=True)

    class Meta:
        verbose_name = 'Категория услуги'
        verbose_name_plural ='Категории услуг'

    def __str__(self):
        return self.title


class TypeOfService(models.Model):
    """Модель описывает тип сервиса"""
    category_of_service_id = models.ForeignKey(CategoryOfService,
                                               on_delete=models.CASCADE,
                                               verbose_name='Категория услуги')
    title = models.CharField(max_length=256, verbose_name='Тип услуги', unique=True)
    image = models.ImageField(verbose_name='Изображение услуги')
    description = models.TextField(verbose_name='Описание услуги')
    best = models.BooleanField(default=False, verbose_name='Продвигаемое')

    class Meta:
        verbose_name = 'Тип услуги'
        verbose_name_plural ='Тип услуг'

    def __str__(self):
        return self.title


class TypeOfSubService(models.Model):
    """Модель содержит в себе уточнение типа сервиса"""
    type_of_service_id = models.ForeignKey(TypeOfService,
                                           on_delete=models.CASCADE,
                                           verbose_name='Тип услуги')
    title = models.CharField(max_length=256, verbose_name='Тип подсервиса')
    unit = models.CharField(max_length=256, verbose_name='Единица измерения')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Стоимость')

    class Meta:
        verbose_name = 'Уточнение услуги'
        verbose_name_plural ='Уточнение услуг'

    def __str__(self):
        return f'{self.title} --- {self.unit} --- {self.price}'
