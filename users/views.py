from django.shortcuts import render, redirect
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy

from django.db.utils import IntegrityError

from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.auth.models import User

from users.forms import ProfileForm, SignupForm
from posts.models import Post
from users.models import Profile

class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'users/detail.html' 
    slug_field='username' # Para ejecutarse necesita una llave primaria, pero en este ejemplo no se tiene eso
    slug_url_kwarg= 'username'
    queryset = User.objects.all()  
    context_object_name='user' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    template_name= 'users/update_profile.html'
    model = Profile
    fields= ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        return self.request.user.profile
    
    def get_success_url(self):
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username':username})
  
class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
   
"""@login_required
def update_profile(request):
    profile = request.user.profile
    
    if request.method =='POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website= data ['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']

            profile.save()
            url = reverse('users:detail', kwargs={'username': request.user.username})
            return redirect (url)          
    else:
        form = ProfileForm()
        
    return render(
        request= request,
        template_name= 'users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )
    return render(request, 'users/update_profile.html')
"""

"""def login_view(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password= password)
        if user:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error': 'Usuario y contraseña invalidos'})
    return render (request, 'users/login.html')"""

class SingupView(FormView):
    template_name = 'users/singup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

"""def singup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('users:login')
    else:
        form = SignupForm()
    return render(
        request = request,
        template_name = 'users/singup.html',
        context={
            'form': form
        }
    )"""

"""@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')"""
    
class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    pass

"""
Esta seria la forma en la que se validaria la información sin tener en cuenta un modelo
def singup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        
        if password != password_confirmation:
            return render(request, 'users/singup.html', {'error': 'Las contraseñas no coinciden'}) 
        try:
            user = User.objects.create_user(username = username, password= password)
        except IntegrityError:
            return render(request, 'users/singup.html', {'error': 'Nombre de usuario ya existe'})
        
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        
        profile = Profile(user=user)
        profile.save()
        return redirect('login')
        
    return render(request, 'users/singup.html')
"""
