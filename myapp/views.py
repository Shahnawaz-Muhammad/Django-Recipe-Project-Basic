from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import CustomUser  # Import the custom user model

# Create your views here.

def home(request):
    people = [
  {
    'id': 1,
    'name': "John Doe",
    'age': 30,
    'address': "123 Main St, Springfield, IL"
  },
  {
    'id': 2,
    'name': "Jane Smith",
    'age': 25,
    'address': "456 Oak St, Lincoln, NE"
  },
  {
    'id': 3,
    'name': "Michael Johnson",
    'age': 35,
    'address': "789 Pine St, Columbus, OH"
  },
  {
    'id': 4,
    'name': "Emily Davis",
    'age': 28,
    'address': "321 Maple St, Madison, WI"
  },
  {
    'id': 5,
    'name': "Robert Brown",
    'age': 40,
    'address': "654 Cedar St, Denver, CO"
  }
]
    for person in people:
        print(person)

    return render(request, 'main/index.html', context={'page': 'Django Learning 2024', 'people': people})

def about(request):
    context={'page': 'About'}
    return render(request, 'main/about.html', context)

def contact(request):
    context={'page': 'Contact'}
    return render(request, 'main/contact.html', context)
  
def login_page(request):
    context={'page': 'Login'}
    if request.method == "POST":
      email = request.POST.get('email')
      password = request.POST.get('password')
            
      if CustomUser.objects.filter(email = email).exists():
        messages.error(request, "User is not recognized! ")
        return redirect('/login/')
      
      user = authenticate(request,  email=email, password = password)
      
      if user is None: 
        messages.error(request, "invalid email or password!")
        return redirect('/login/')

      else: 
        login(request, user)
        return redirect('/recipes/')
      
      
    return render(request, 'auth/login.html', context)
  
    
def register(request):
    context={'page': 'Register'}
    if request.method == "POST":
      first_name = request.POST.get('first_name')
      last_name = request.POST.get('last_name')
      email = request.POST.get('email')
      password = request.POST.get('password')
      confirm_password = request.POST.get('confirm_password')
      
      user = User.objects.filter(email = email)
      
      if password != confirm_password:
        messages.error(request, "Passwords do not match.")
        return redirect('/register/')

      if user.exists():
        messages.warning(request, "User already exits!. ")
        return redirect('/register/')
      
      user = User.objects.create(
        first_name = first_name,
        last_name = last_name,
        email=email,
        username = email,
        )
      
      user.set_password(password)
      user.save()
      
      messages.success(request, "User created Successfull!")
      
      return redirect('/register/')

    return render(request, 'auth/register.html', context)