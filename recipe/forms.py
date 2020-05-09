from django import forms
from recipe.models import Author


class RecipeAddForm(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea)
    time = forms.CharField(max_length=20)
    instructions = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())

class AuthorAddForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
# #
# class AuthorAddForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = [
#             'name',
#             'bio',
#
#         ]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

