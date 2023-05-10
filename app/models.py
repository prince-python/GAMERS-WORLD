from django.db import models
from django.utils.timezone import datetime
# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=254)
    email= models.EmailField( max_length=254)
    pwd=models.CharField(max_length=300)
    d = models.DateTimeField( auto_now_add=True)
    def __str__(self):
        return self.name



class Game(models.Model):
    title=models.CharField(max_length=200 ,blank=False)
    description=models.CharField(max_length=1000, blank=False)
    link=models.CharField(max_length=10000)
    orignalsize=models.CharField(max_length=10000)
    Repacksize=models.CharField(max_length=10000)
    img=models.ImageField(upload_to='game/')
    d = models.DateTimeField( auto_now_add=True)
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    User= models.ForeignKey(User, on_delete=models.CASCADE)
    comment=models.CharField(max_length=1000000)
    d = models.DateTimeField( auto_now_add=True)
    Game=models.ForeignKey(Game,on_delete=models.CASCADE)
    def __str__(self):
        return self.comment
    
    
class Images(models.Model):
    name=models.CharField(max_length=200)
    images=models.FileField(upload_to='images/')
    d = models.DateTimeField( auto_now_add=True)
    def __str__(self):
        return self.comment
    
    
    
class like(models.Model):
    Comment=models.ForeignKey(Comment, on_delete=models.CASCADE)