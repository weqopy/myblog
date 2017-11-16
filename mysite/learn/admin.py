from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'update_date')


admin.site.register(Article, ArticleAdmin)
