from django.shortcuts import render, get_object_or_404,reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from recipe.models import Author, Recipe
from recipe.forms import RecipeAddForm, AuthorAddForm, LoginForm





def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'genericform.html', {'form': form})

@login_required()
def logged_outview(request):
    logout(request)
    return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))


def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

@login_required
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

# I was able to find the staff_member_required decorator on stackoverflow
@staff_member_required()
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
