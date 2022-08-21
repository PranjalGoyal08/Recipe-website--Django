# from logging import PlaceHolder
from ast import Delete
from dataclasses import field
from pyexpat import model
from django import forms
from django.forms.models import inlineformset_factory
from .models import Post, RecipeIngrident, Ingrident



class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ('title', 'author','description','recipe_image','body')

        widgets = {
            'title': forms.TextInput(attrs={'class':"form-control",'placeholder':"Name of your recipe"}),
            'author': forms.TextInput(attrs={'class':"form-control",'value':" ", 'id':"elder",'type':"hidden"}),
            # 'ingridents': forms.Textarea(attrs={'class':"form-control",'PlaceHolder':"Ingrident-Qunatity"}),
            'body': forms.Textarea(attrs={'class':"form-control", 'placeholder':"method for makeing the recipe"}),
            'description': forms.Textarea(attrs={'class':"form-control",'PlaceHolder':"About Your Recipe"}),
        }

class IngridentForm(forms.ModelForm):
    class Meta:
        model= Ingrident
        fields =('name',)

class RecipeIngridentForm(forms.ModelForm):
    class Meta:
        model = RecipeIngrident
        exclude=('recipe',)
IngredientFormSet =inlineformset_factory(Post, RecipeIngrident, form=RecipeIngridentForm, can_delete=True, extra=6)


class EditForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ('title', 'description', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':"form-control"}),
            # 'author': forms.Select(attrs={'class':"form-control"}),
            'description': forms.Textarea(attrs={'class':"form-control",'PlaceHolder':"About Your Recipe"}),
            'body': forms.Textarea(attrs={'class':"form-control"}),

        }