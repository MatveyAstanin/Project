from django.db import models

class Games(models.Model):

    # Fields
    game_name = models.CharField(null=True, max_length=100,  help_text="Enter field documentation", verbose_name="Название игры")
    game_image = models.TextField(null=True, blank=True, verbose_name="Картинка игры")
    game_about = models.TextField(null=True,  blank=True, verbose_name="Описание игры")
    game_price = models.FloatField(null=True, blank=True, verbose_name="Цена игры")
    game_valid = models.BooleanField(null=True, verbose_name="Вышла или не вышла игра")
    game_published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата добавление игры")
    game_sale = models.BooleanField(null=True, verbose_name="Скидка")
    # Metadata
    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ["-game_published"]
