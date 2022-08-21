from distutils.command.upload import upload
from hashlib import blake2b
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField



# INGRIDENT_CHOICES = (
#     ("salt", "Salt"),
#     ("sugar", "Sugar"),
#     ("flour", "Flour"),
#     ("turmeric", "Turmeri"),
#     ("cocopowder", "Coco Powder"),
#     ("milk", "Milk"),
#     ("bakingpowder", "Baking Powder"),
#     # ("8", "8"),
# )



class Post(models.Model):
    
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    recipe_image= models.ImageField(null=True, blank= True, upload_to= "images/")
    # ingridents = models.TextField()
    ingridents= RichTextField(blank=  True, null= True)
    body= RichTextField(blank=  True, null= True)
    description = models.CharField(max_length=800)
    post_date= models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="recipe_post", blank=True)
    unlikes = models.ManyToManyField(User, related_name="unlike_post", blank=True)




    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
    
    def total_likes(self):
        return self.likes.count()

    def total_unlikes(self):
        return self.unlikes.count()

class Ingrident(models.Model):
    name= models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')

# ingridentname = Ingridentnames.objects.all()
# list=[]
# for i in ingridentname:
#     list.append(str(i))
# # print(list)
# # tuple1 = tuple(i for i in list)
# # print(tuple1)
# tuple2= tuple(zip(list,list))
# print(tuple2)


class RecipeIngrident(models.Model):
    ingredient = models.ForeignKey(Ingrident, on_delete=models.CASCADE, related_name='ingrident', null=True)
    quantity= models.FloatField()
    unit = models.CharField(max_length=5)

    recipe = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ingrident', null=True)
    
    def __str__(self):
        return str(self.ingredient)

    def getQuantity(self):    
        return str(self.quantity)

    def getUnit(self):
        return str(self.unit)
    
    def get_recipe(self):
        return self.recipe

    
