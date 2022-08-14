from django.urls import path
from .views import trendingmovies, HomePage, Register, Login, test, logoutuser , add_movies,home,record
from . import views as u_views
from . import views
from .views import video




urlpatterns = [
    #path converters
    # int: numbers
    # str: strings
    #path: Whole urls /

    path('home/', HomePage, name="home-page"),
    path('register/', Register, name="register-page"),
    path('login/', Login, name="login-page"),
    path('logout/', logoutuser, name='logout'),
    path('test/', test, name='test'),
    path('home/',home,name='home'),
    path('add_movies/',add_movies,name='add_movies'),
    path('add_movies/record/',record,name='record'),
    path('trendingmovies/', trendingmovies,name='trendingmovies'),
    #path('aboutus/', aboutus,name='aboutus'),
    path('', video),
]