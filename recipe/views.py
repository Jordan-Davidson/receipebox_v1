from django.shortcuts import render, get_object_or_404
from recipe.models import Author, Recipe




# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    recipes = Recipe.objects.filter(author=author)
    return render(request, 'author.html', {'author': author, 'recipes': recipes})
