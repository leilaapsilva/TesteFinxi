# Generated by Django 3.0.8 on 2020-08-05 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finxiapp', '0003_demandadepecas_anunciante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandadepecas',
            name='descricao',
            field=models.CharField(max_length=200, verbose_name='Descrição'),
        ),
    ]
