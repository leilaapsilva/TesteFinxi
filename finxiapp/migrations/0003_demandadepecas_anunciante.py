# Generated by Django 3.0.8 on 2020-08-05 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finxiapp', '0002_auto_20200805_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='demandadepecas',
            name='anunciante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finxiapp.Anunciante'),
        ),
    ]
