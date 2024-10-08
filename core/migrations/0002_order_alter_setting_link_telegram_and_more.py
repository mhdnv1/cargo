# Generated by Django 5.1 on 2024-08-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон номер')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')),
                ('is_done', models.BooleanField(default=False, verbose_name='Активнось')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.AlterField(
            model_name='setting',
            name='link_telegram',
            field=models.URLField(verbose_name='Телеграм ссылка'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='link_whatsapp',
            field=models.URLField(verbose_name='Ватсап ссылка'),
        ),
    ]
