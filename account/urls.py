from django.urls import path
from . import views


urlpatterns = [
    path("login", views.sign_in),
    path("logout", views.logout_view),
    path("register", views.register_view)

]