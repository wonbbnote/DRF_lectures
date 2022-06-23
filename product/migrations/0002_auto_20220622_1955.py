# Generated by Django 3.2.5 on 2022-06-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='activation',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='modified_date',
            field=models.DateField(null=True, verbose_name='수정 일자'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True, verbose_name='가격'),
        ),
    ]