from django.shortcuts import render, get_object_or_404,reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from recipe.models import Author, Recipe
from recipe.forms import RecipeAddForm, AuthorAddForm, LoginForm, EditRecipe

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def recipeadd(request):
    html = 'genericform.html'

    if request.method == "POST":
        form = RecipeAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                description=data['description'],
                time=data['time'],
                instructions=data['instructions'],
                author=data['author']

            )
            return HttpResponseRedirect(reverse('homepage'))

    form = RecipeAddForm()

    return render(request, html, {'form': form})


def authoradd(request):
    html = 'genericform.html'

    if request.method == 'POST':
        form = AuthorAddForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = AuthorAddForm()

    return render (request, html, {'form': form})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    recipes = Recipe.objects.filter(author=author)
    return render(request, 'author.html', {'author': author, 'recipes': recipes})


def loginUser(request):
    html = 'login.html'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
    form = LoginForm()
    return render(request, html, {'form': form})

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def signup(request):
    html = 'login.html'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
    form = LoginForm()
    return render(request, html, {'form': form})

@login_required
def editRecipe(request, id):
    html = 'genericform.html'
    recipe = Recipe.objects.get(id=id)
    if request.method == 'POST':
        form = EditRecipe(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            recipe.title = data['title']
            recipe.description = data['description']
            recipe.time = data['time']
            recipe.instructions = data['instructions']
            recipe.save()
            return HttpResponseRedirect(reverse('recipe_detail', args=(id, )))
    form = EditRecipe(initial={
        'title': recipe.title,
        'description': recipe.description,
        'time': recipe.time,
        'instructions': recipe.instructions,
    })
    return render(request, html, {'form': form})

@login_required
def addFavorite(request, id):
    recipe = Recipe.objects.get(id=id)
    request.user.author.favorites.add(recipe)
    return HttpResponseRedirect(reverse('recipe_detail', args=(id, )))

def favorites(request, id):
    html = 'favorites.html'
    author = Author.objects.get(id=id)
    favorites = author.favorites.all()
    return render(request, html, {'favorites': favorites})
