from django.test import TestCase

# Create your tests here.
from .models import Category, Website

def index(request):
  categories = Category.objects.all()
  return render(request, 'index.html', {'categories': categories})

def category(request, id):
  category = Category.objects.get(id=id)
  websites = Website.objects.filter(category=category)
  return render(request, 'category.html', {'category': category, 'websites': websites})