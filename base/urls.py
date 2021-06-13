from django.urls import path
from .views import PostList,PostDetail,PostCreate,UserLoginView,Profile
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.registerPage, name='register'),
    path('profile/', Profile.as_view(), name='profile'),
    path('', PostList.as_view(), name='posts'),
    path('post/<int:pk>', PostDetail.as_view(), name='post'),
    path('post-create/', PostCreate.as_view(), name='post-create'),
    path('profile-edit/',views.profileUpdate, name='profile-edit'),
]