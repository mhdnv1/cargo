# Generated by Django 5.1 on 2024-08-26 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_contact_remove_setting_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='Почта Админа'),
            preserve_default=False,
        ),
    ]
