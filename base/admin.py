from django.contrib import admin
from .models import Post,Ingrident, RecipeIngrident

# Register your models here.
class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngrident

@admin.register(Post)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline, ]

admin.site.register(Ingrident)
