from django.urls import path

from .views import index, signupUser, loginUser, logoutUser, loadProfile

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signupUser, name='signup'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('profile/<str:username>/', loadProfile, name='loadProfile')
]