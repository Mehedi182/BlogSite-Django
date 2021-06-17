from django.urls import path
from .views import PostList,PostCreate,UserLoginView,Profile,UserDetail
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    path('', PostList.as_view(), name='posts'),
    path('register/', views.registerPage, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', Profile.as_view(), name='profile'),
    path('profile-edit/', views.profileUpdate, name='profile-edit'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post-create/',PostCreate.as_view(), name='post-create'),
    path('writters/<int:pk>/', UserDetail.as_view(), name='writters'),

]