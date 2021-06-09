from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from .forms import CreateUserForm
from .models import Post


class PostList(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post'


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','intro','description', 'img']
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)


class TaskCreate(LoginRequiredMixin,CreateView):
    model = Post
    fields =['title','description']
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)


class UserLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('posts')


def userprofile(request):
    if request.user.is_authenticated:
        user = request.user
        template_name = 'base/profile.html'
        post_obj = Post.objects.filter(pk=user.id)
        context = {'post_obj':post_obj}
        return render(request,template_name,context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('posts')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'base/register.html', context)


