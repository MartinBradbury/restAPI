from django.urls import path
from Profiles import views

urlpatterns = [
    path('users/', views.CustomUserList.as_view(), name='custom_user_list'),
    path('profiles/', views.UserProfileList.as_view(), name='profile_list'),

]