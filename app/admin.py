from django.contrib import admin
from app import models

admin.site.register(models.Movies)
admin.site.register(models.Ticket)
admin.site.register(models.Customer)
admin.site.register(models.Places)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title')
    prepopulated_fields = {"slug": "title"}
