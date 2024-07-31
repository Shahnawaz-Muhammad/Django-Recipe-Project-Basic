from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
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
  
def login(request):
    context={'page': 'Login'}
    return render(request, 'auth/login.html', context)
  
    
def register(request):
  if request.method == "POST":
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = User.objects.filter(username = username)

    if user.exists():
      messages.warning(request, "User already exits!. ")
      return redirect('/register/')
    
    user = User.objects.create(
      first_name = first_name,
      last_name = last_name,
      username = username,
      )
    
    user.set_password(password)
    user.save()
    
    messages.success(request, "User created Successfull!")
    
    return redirect('/register/')

  return render(request, 'auth/register.html')