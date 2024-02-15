from django.urls import path
from . import views

app_name = "Blog"
urlpatterns = [
    path('detail/<slug:slug>', views.detail_page, name="article_detail"),
    path('list', views.articles_page, name="articles_page"),
    path('category/<int:pk>', views.category_articles, name="category_articles"),
    path('search/', views.search, name="search"),
    path('contactus', views.contactus, name="contactus")
]