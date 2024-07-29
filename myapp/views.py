from django.shortcuts import render
from django.http import HttpResponse
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