from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, RecipeCategory


@admin.register(RecipeCategory)
class RecipeCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
    )
    list_filter = (
        'name',
        'description',
    )
    search_fields = (
        'name',
        'description',
    )


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = (
        'title',
        'category',
        'calories',
        'cooking_time',
        'food_intake'
    )
    list_filter = (
        'category',
        'food_intake',
    )
    readonly_fields = (
        'calories',
    )
    search_fields = (
        'title',
        'description',
        'cooking_method'
    )

    def calories(self, obj):
        return obj.get_total_calories()


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'calories_per_100g',
        'allergic_category',
    )
    list_filter = (
        'name',
        'calories_per_100g',
        'allergic_category',
    )
    search_fields = (
        'name',
        'calories_per_100g',
        'allergic_category',
    )
