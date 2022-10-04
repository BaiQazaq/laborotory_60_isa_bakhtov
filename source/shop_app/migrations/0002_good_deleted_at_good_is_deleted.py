# Generated by Django 4.1.1 on 2022-10-04 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True, verbose_name='Дата удаления'),
        ),
        migrations.AddField(
            model_name='good',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Удалено'),
        ),
    ]