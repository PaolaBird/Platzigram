from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
#from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from posts.forms import PostForm

from posts.models import Post

# posts = posts = [
#     {
#         'title': 'Mont Blanc',
#         'user': {
#             'name': 'Yésica Cortés',
#             'picture': 'https://picsum.photos/60/60/?image=1027'
#         },
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/800/600?image=1036',
#     },
#     {
#         'title': 'Via Láctea',
#         'user': {
#             'name': 'Christian Van der Henst',
#             'picture': 'https://picsum.photos/60/60/?image=1005'
#         },
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/800/800/?image=903',
#     },
#     {
#         'title': 'Nuevo auditorio',
#         'user': {
#             'name': 'Uriel (thespianartist)',
#             'picture': 'https://picsum.photos/60/60/?image=883'
#         },
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/500/700/?image=1076',
#     }
# ]

class PostFeedView(LoginRequiredMixin, ListView):
    template_name = 'posts/feed.html'
    model= Post
    ordering = ('-created',)
    paginate_by= 30
    context_object_name='posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'
 
class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context
    
"""@login_required
def list_posts(request):
    # content = []
    # for post in posts:
    #     content.append('
    #                    <p><strong>{name}</strong></p>
    #                    <p><small>{user}<i>{timestamp}</i></small></p>
    #                    <figure><img src="{picture}"/></figure>
    #                    .format(**post)) #Desempaqueta el arreglo de post y no es necesario decir que por ejemplo name=posts['name']'
    # return HttpResponse('<br>'.join(content))
    #Del ultimo al primero agregado
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {'posts': posts})"""

"""@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()
    return render(
        request = request,
        template_name = 'posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )"""