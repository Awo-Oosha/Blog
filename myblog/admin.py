from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

my_models = [models.Category, models.Comment, models.Tag]

for item in my_models:
    admin.site.register(item)
