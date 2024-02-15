from django.db import models
from django.contrib.auth.models import User
# from .managers import IsStar_manager
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    subcategory = models.CharField(max_length=20)

    def __str__(self):
        return self.subcategory


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=50)
    descr = models.TextField()
    image = models.ImageField(upload_to='index/images', blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    star = models.BooleanField()
    # objects = models.Manager()
    # starManager = IsStar_manager()
    slug = models.SlugField(null=True, blank=True, unique=True)

    def get_absolute_url(self):
        return reverse('Blog:article_detail', args=[self.slug])

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Article, self).save()


    def __str__(self):
        return f"{self.title} - {self.category}"

    class Meta:
        verbose_name = "مطلب"
        verbose_name_plural = "مطالب"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True, blank=True, related_name='replies')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:30]