
from django.urls import path
from . import views 
urlpatterns = [
    path('', views.form, name="form"),
    path('about', views.about, name="about"),
    path('wishes', views.wishes, name="wishes")
]
