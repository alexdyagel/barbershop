# Generated by Django 2.2.1 on 2019-05-07 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190507_2101'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'order', 'verbose_name_plural': 'orders'},
        ),
        migrations.AlterModelOptions(
            name='seance',
            options={'verbose_name': 'seance', 'verbose_name_plural': 'seances'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'service', 'verbose_name_plural': 'services'},
        ),
        migrations.AlterModelOptions(
            name='specialist',
            options={'verbose_name': 'specialist', 'verbose_name_plural': 'specialists'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Category name.', max_length=25, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(help_text='Service name.', max_length=25, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='name',
            field=models.CharField(help_text='Specialist name.', max_length=25, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='position',
            field=models.CharField(help_text='Position of specialist.', max_length=25, verbose_name='position'),
        ),
    ]
