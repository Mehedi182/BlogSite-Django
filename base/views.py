from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import CommentForm, CreateUserForm, UserUpdateForm
from .models import Post, Comment, User


class PostList(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'intro', 'description', 'img']
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)


class UserLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('posts')


class Profile(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'base/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['posts'].filter(user=self.request.user)
        return context


class UserDetail(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'base/user_detail.html'
    context_object_name = 'user'


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


def profileUpdate(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)

            def __init__(self, *args, **kwargs):
                self.fields['user'].widget.attrs['readonly'] = True

            if u_form.is_valid():
                u_form.save()
                messages.success(request, f'Your account has been updated!')
                return redirect('profile')

        else:
            u_form = UserUpdateForm(instance=request.user)
        context = {
            'u_form': u_form,
        }

        return render(request, 'base/profile_edit.html', context)
    else:
        return redirect('login')


def post_detail(request, pk):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=pk)
        if request.method == 'POST':
            form = CommentForm(request.POST)

            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.user = request.user
                comment.save()

                return redirect('post_detail', pk=post.pk)
        else:
            form = CommentForm()

        return render(request, 'base/post_detail.html', {'post': post, 'form': form})

    else:
        return redirect('login')
