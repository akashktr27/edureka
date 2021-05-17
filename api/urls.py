from django.urls import path
from .views import (home, about, signup, login)

urlpatterns = [
    path('', home),
    path('about/', about, name='abt'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login')

]