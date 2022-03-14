from django.urls import path
from . import views

urlpatterns = [
  #Pat Blog
  path('', views.blog, name="blog"),
  path('category/<int:category_id>/', views.category, name="category"),
]