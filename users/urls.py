from django.urls import path
#from django.views.generic import TemplateView

from users import views


urlpatterns = [
    #path('<str:username>/', TemplateView.as_view(template_name='users/detail.html'), name='detail'),
    path('<str:username>/', views.UserDetailView.as_view(), name= 'detail'),
    path('users/login/', views.LoginView.as_view(), name='login'),
    path('users/logout/', views.LogoutView.as_view(), name='logout'),
    path('users/singup/', views.SingupView.as_view(), name='singup'),
    path('users/me/profile', views.UpdateProfileView.as_view(), name='update')
]