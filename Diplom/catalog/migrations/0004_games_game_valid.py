# Generated by Django 3.0 on 2021-02-10 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20210211_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='game_valid',
            field=models.BooleanField(null=True, verbose_name='Вышла или не вышла игра'),
        ),
    ]