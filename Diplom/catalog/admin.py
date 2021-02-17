from django.contrib import admin
from .models import Games


class GamesAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'game_image', 'game_about', 'game_price', 'game_published', 'game_valid', 'game_sale')
    list_display_links = ('game_name', 'game_about')
    search_fields = ('game_name', 'game_about', )


admin.site.register(Games, GamesAdmin)
