from django.urls import path
from scroll import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='index')
]
