from distutils.command.upload import upload
from hashlib import blake2b
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    recipe_image= models.ImageField(null=True, blank= True, upload_to= "images/")
    # ingridents = models.TextField()
    ingridents= RichTextField(blank=  True, null= True)
    body= RichTextField(blank=  True, null= True)
    description = models.CharField(max_length=800)
    post_date= models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="recipe_post")
    unlikes = models.ManyToManyField(User, related_name="unlike_post")


    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
    
    def total_likes(self):
        return self.likes.count()

    def total_unlikes(self):
        return self.unlikes.count()