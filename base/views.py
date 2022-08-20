from json import JSONDecoder
from django.db import transaction
import imp
from multiprocessing import context
from django.shortcuts import render, get_object_or_404,  redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Post,RecipeIngrident
from  base import models
from .forms import PostForm, EditForm, IngredientFormSet
from django.urls import reverse_lazy, reverse

# Create your views here.


class HomeView(ListView):
    model=Post
    template_name ='home.html'
    ordering=['-post_date']

class ArticleDetailView(DetailView):
    model= Post
    # context_object_name= 'article-detail'
    

    template_name = 'article_detail.html'
    # queryset= Post
    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        stuff= get_object_or_404(Post, id=self.kwargs['pk'])
        # ingdData = RecipeIngrident.objects.all()
        # ingdetail= ingdData[0].get_recipe()
        # print("DEBUG2: ", ingdetail)
        # # for ingDa in ingdData:
        # #     print("Debug2: ", ingDa)
        ingrident_info=[]
        ingdData = RecipeIngrident.objects.all()
        postData = Post.objects.get(id=self.kwargs['pk'])

        # unit= ingdData[0].unit()
        # print(unit)
        for i in range (len(ingdData)):
            if(ingdData[i].get_recipe()==postData):
                # print("Debug : ", ingdData[i])
                # print("Debug: ", )

                ingrident_info.append({'name':str(ingdData[i]), 'unit':ingdData[i].getUnit(), 'quantity':str(ingdData[i].getQuantity())})
        # print(ingrident_info)
        # print(len(ingrident_info))
        context["ingrident_info"]=ingrident_info
        liked= False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked= True

        unliked= False
        if stuff.unlikes.filter(id=self.request.user.id).exists():
            unliked= True

        total_unlikes= stuff.total_unlikes()
        # print(total_unlikes)
        context["total_unlikes"] = total_unlikes
        context["unliked"]=unliked


        total_likes= stuff.total_likes()
        context["total_likes"] = total_likes
        context["liked"]=liked
        return context


class AddRecipeView(CreateView):
    model= Post
    form_class = PostForm
    template_name = 'addRecipe.html'
    #fields = '__all__'
    #fields = ('title','body')

class UpdateRecipeView(UpdateView):
    model= Post
    form_class= EditForm
    template_name = 'update_recipe.html'
    # fields = ('title','body')

class DeleteRecipeView(DeleteView):
    model= Post
    template_name = 'delete_recipe.html'
    success_url= reverse_lazy('home')


class SearchResultView(ListView):
    model = Post
    template_name = "search.html"
    # context_object_name= "posts"
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list =  Post.objects.filter(title__icontains= query)
        return object_list

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked= False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked= False
    else:
        post.likes.add(request.user)
        liked= True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

def UnlikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    unliked= False
    if post.unlikes.filter(id=request.user.id).exists():
        post.unlikes.remove(request.user)
        unliked= False
    else:
        post.unlikes.add(request.user)
        unliked= True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

def create_ingrident_recipe(request):
    if request.method == "GET":
        form = PostForm()
        formset = IngredientFormSet()
        return render(request, 'addingrident.html', {"form":form, "formset":formset})
    elif request.method =="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            formset = IngredientFormSet(request.POST, instance=recipe)
            if formset.is_valid():
                formset.save()
            return redirect('/')
        else:
            return render(request, 'addingrident.html', {"form":form})
