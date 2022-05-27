from django.shortcuts import render, get_object_or_404
from .models import recipes as Recipes

def all_recipes(request):
    recipes=Recipes.objects.all()
    return render(request,'component/all_recipes.html',{'recipes':recipes})
def detail_recipe(request,recipe_id):
    recipe=get_object_or_404(Recipes,pk=recipe_id)
    return render(request,'component/detail_recipe.html',{'recipe':recipe})
