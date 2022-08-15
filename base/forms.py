# from logging import PlaceHolder
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ('title', 'author','description','recipe_image','ingridents', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':"form-control",'placeholder':"Name of your recipe"}),
            'author': forms.TextInput(attrs={'class':"form-control",'value':" ", 'id':"elder",'type':"hidden"}),
            'ingridents': forms.Textarea(attrs={'class':"form-control",'PlaceHolder':"Ingrident-Qunatity"}),
            'body': forms.Textarea(attrs={'class':"form-control", 'placeholder':"method for makeing the recipe"}),
            'description': forms.Textarea(attrs={'class':"form-control",'PlaceHolder':"About Your Recipe"}),
             
        }

class EditForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ('title', 'description','ingridents', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':"form-control"}),
            # 'author': forms.Select(attrs={'class':"form-control"}),
            'description': forms.Textarea(attrs={'class':"form-control",'PlaceHolder':"About Your Recipe"}),
            'ingridents': forms.Textarea(attrs={'class':"form-control",'PlaceHolder':"Ingrident-Qunatity"}),
            'body': forms.Textarea(attrs={'class':"form-control"}),

        }