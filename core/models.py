from django.db import models

# Create your models here.


class Setting(models.Model):
    
    title = models.CharField(verbose_name='Название сайта', max_length=255)
    phone = models.CharField(verbose_name='Телефон номер', max_length=255)
    link_whatsapp = models.URLField(verbose_name='Ватсап ссылка')
    link_telegram = models.URLField(verbose_name='Телеграм ссылка')
    email = models.EmailField(verbose_name='Почта Админа')
    

    class Meta:

        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'

    def __str__(self):
        return f'Натройка {self.id}'



class Section(models.Model):
    
    section = models.CharField(verbose_name='Название раздел',max_length=255)
    title = models.CharField(verbose_name='Заголовок',max_length=255)
    text = models.TextField(verbose_name='Текст')
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE, verbose_name='Настрока', related_name='sections')
    
    def __str__(self) -> str:
        return f'Раздел {self.title}'
    
 
class Order(models.Model):
    
    phone = models.CharField(verbose_name='Телефон номер', max_length=255)
    date = models.DateTimeField(verbose_name='Дата и время', auto_now_add=True)
    is_done = models.BooleanField(verbose_name='Активнось', default=False)
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        
    def __str__(self):
        return f'Заказ №{self.id}'
    

class ServicePrice(models.Model):
    
    country = models.CharField(verbose_name='Страна', max_length=255)
    text = models.TextField(verbose_name='Об услуге')
    price = models.CharField(verbose_name='цена за кг', max_length=255)
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        
    def __str__(self) -> str:
        return f'Страна - {self.country}, Цена {self.price} за 1кг '
    
class Album(models.Model):
    
    image = models.ImageField(verbose_name='Фото', upload_to='album/')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Альбом'
        
    def __str__(self) -> str:
        return f'Фото №{self.id}'
    


class Contact(models.Model):
    
    location = models.CharField(verbose_name='Филиал',max_length=255)
    phone = models.CharField(verbose_name='Телефон номер', max_length=255)
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        
    def __str__(self):
        return f'{self.location} - {self.phone}'
    