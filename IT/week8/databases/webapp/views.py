
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

from django.http import JsonResponse
def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    websites = Website.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'websites': websites})
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the index view after saving
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})
def add_website(request):
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            website = form.save(commit=False)
            category = get_object_or_404(Category, id=request.POST.get('category'))
            website.category = category
            website.save()
            return redirect('index')
    else:
        form = WebsiteForm()
    categories = Category.objects.all()
    return render(request, 'add_website.html', {'form': form, 'categories': categories})

def insert_works(request):
    if request.method == 'POST':
        person_name = request.POST.get('person_name')
        company_name = request.POST.get('company_name')
        salary = request.POST.get('salary')
        Works.objects.create(person_name=person_name, company_name=company_name, salary=salary)
    return render(request, 'insert_works.html')

def retrieve_works_lives(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        works_data = Works.objects.filter(company_name=company_name)
        lives_data = Lives.objects.filter(person_name__in=[work.person_name for work in works_data])
        context = {'works_data': works_data, 'lives_data': lives_data}
    else:
        context = {}
    return render(request, 'retrieve_works_lives.html', context)

def add_data(request):
    author_form = AuthorForm(request.POST or None)
    publisher_form = PublisherForm(request.POST or None)
    book_form = BookForm(request.POST or None)
    if request.method == 'POST':
        if author_form.is_valid():
            author_form.save()
        if publisher_form.is_valid():
            publisher_form.save()
        if book_form.is_valid():
            book_form.save()
    context = {'author_form': author_form, 'publisher_form': publisher_form, 'book_form': book_form}
    return render(request, 'add_data.html', context)

def retrieve_data(request):
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    books = Book.objects.all()
    context = {'authors': authors, 'publishers': publishers, 'books': books}
    return render(request, 'retrieve_data.html', context)

def index2(request):
    products = Product.objects.all()
    return render(request, 'index2.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index2')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def human_view(request):
    humans = Human.objects.all()
    context = {
        'humans': humans
    }

    if request.method == 'POST':
        if 'update' in request.POST:
            id = request.POST.get('id')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            city = request.POST.get('city')

            human = Human.objects.get(id=id)
            human.first_name = first_name
            human.last_name = last_name
            human.phone = phone
            human.address = address
            human.city = city
            human.save()

        elif 'delete' in request.POST:
            id = request.POST.get('id')
            human = Human.objects.get(id=id)
            human.delete()

    return render(request, 'human.html', context)


def get_human(request, id):
    human = Human.objects.get(id=id)
    data = {
        'last_name': human.last_name,
        'phone': human.phone,
        'address': human.address,
        'city': human.city,
    }
    return JsonResponse(data)