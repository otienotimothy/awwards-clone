from django.urls import path

from .views import index, signupUser, loginUser

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signupUser, name='signup'),
    path('login/', loginUser, name='login')
]