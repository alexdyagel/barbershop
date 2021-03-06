# Generated by Django 2.2.1 on 2019-05-07 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190508_0137'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'услуга', 'verbose_name_plural': 'услуги'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Название категории', max_length=25, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(help_text='Название услуги.', max_length=25, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Цена услуги.', max_digits=6, verbose_name='цена'),
        ),
    ]
