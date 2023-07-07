from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    subcategory = models.CharField(max_length=20)

    def __str__(self):
        return self.subcategory


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=50)
    descr = models.TextField()
    image = models.ImageField(upload_to='Home/images', blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title