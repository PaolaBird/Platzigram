from django.urls import path
from django.views.generic import TemplateView

from posts import views

urlpatterns =[
    path('', views.PostFeedView.as_view(), name='feed'),
    path('posts/new/', views.CreatePostView.as_view(), name='create'), 
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='detail'),   
    path('posts/featured/', TemplateView.as_view(template_name='posts/featured.html'), name='featured')
]