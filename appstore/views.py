from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import context, loader
from .models import movies
from django.urls import path
from .models import Item
#from django.contrib.auth import trendingmovies
# Create your views here.


@login_required
def HomePage(request):
    return render(request, 'auth_system/index.html', {})

def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('sname')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        new_user = User.objects.create_user(name, email, password)
        new_user.first_name = fname
        new_user.last_name = lname

        new_user.save()
        return redirect('home')
  
    return render(request, 'auth_system/register.html', {})

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Error, user does not exist')


    return render(request, 'auth_system/login.html', {})

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({},request))

def add_movies(request):
    template = loader.get_template('movies.html')
    
    return HttpResponse(template.render({},request))    

def trendingmovies(request):
    template = loader.get_template('auth_system/trendingmovies.html')
    movies_list = movies.objects.all().values()
    content={ 'movies_list' : movies_list,}
    
    
    return HttpResponse(template.render(content,request))     


def record(request):
    title= request.POST['title']
    main_actor_= request.POST['main_actor']
    genre= request.POST['genre']
    description= request.POST['description']
    released_date= request.POST.get('released_date')
    movies= request.FILES.get('movies')
    thumbnail= request.FILES.get('thumbnail')
    user_id= request.POST['user_id']

    nvideo = movies(title=title,main_actor=main_actor,genre=genre,description=description,released_date=released_date,video=movies,thumbnail=thumbnail,user_id=user_id)
    nvideo.save()
    return HttpResponseRedirect(reserve['movies'])



def logoutuser(request):
    logout(request)
    return redirect('login-page')

def test(request):
    return render(request, 'auth_system/test.html', {})


def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	total_customers = customers.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending ,
    'video':Item,}
    

	return render(request, 'accounts/dashboard.html', context)
 
def video(request): 
    obj=Item.objects.all()
    return render(request,'video.html',{})