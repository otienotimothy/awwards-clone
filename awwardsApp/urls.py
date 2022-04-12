from unicodedata import name
from django.urls import path

from .views import index, signupUser, loginUser, logoutUser, loadProfile, editProfile, uploadProject, reviewProject

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signupUser, name='signup'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('upload/', uploadProject, name='upload'),
    path('profile/<str:username>/', loadProfile, name='loadProfile'),
    path('profile/edit/', editProfile, name='editProfile'),
    path('rating/<int:projectId>/', reviewProject, name='rating' )
]