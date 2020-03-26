from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="homepage"),
    path('about.html',views.about,name="about"),
]
