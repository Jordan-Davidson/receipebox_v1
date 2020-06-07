from django.urls import path
from recipe import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipeadd/', views.recipeadd),
    path('authoradd/', views.authoradd),
    path('author/<int:pk>/', views.author_detail, name='author'),
    path('login/', views.loginUser),
    path('signup/', views.signup),
    path('logout/', views.logoutUser),
    path('edit/<int:id>/', views.editRecipe),
    path('favorite/<int:id>/', views.addFavorite),
    path('favorites/<int:id>/', views.favorites)
]
