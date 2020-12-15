from django.urls import path
from singleapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sections/<int:num>', views.section, name='section')
]
