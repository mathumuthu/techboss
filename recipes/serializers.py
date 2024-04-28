from rest_framework import serializers
from .models import FoodRecipe

class FoodRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodRecipe
        fields = ['title', 'recipe_type']