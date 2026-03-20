from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.index , name="index"),
    path("post/<slug:slug>", views.details, name="details"),
    path("new_page", views.new_url, name="new_url_page"),
    path("old_url", views.old_url, name="old_url"),
    path("contact", views.contact_view, name="contact") ,
    path("about", views.about_view, name="about")
] 