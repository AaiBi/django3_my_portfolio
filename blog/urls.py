from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blog, name='all_blog'),
    path('<int:post_id>/', views.blog_detail, name='blog_detail'),
]
