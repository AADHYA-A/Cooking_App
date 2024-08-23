# recipes/views.py
from django.shortcuts import render, redirect
from .forms import RecipeForm
from .models import Recipe

def recipe_main(request):
    return render(request, 'recipe.html')

def submit_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'submit_recipe.html', {'form': form})

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})