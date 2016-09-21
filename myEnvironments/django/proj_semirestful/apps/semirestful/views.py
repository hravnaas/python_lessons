from django.shortcuts import render, redirect
from .models import Product

# index: Display all products
def index(request):
    return render(request, 'semirestful/index.html', { "products" :  Product.objects.all() } )

# show: Display a particular product
def show(request, id):
    pass

# new: Display a form to create a new product
def new(request):
    return render(request, 'semirestful/new_product.html')

# edit: Display a form to update a product
def edit(request, id):
    pass

# create: Process information to create a new product
def create(request):
    if request.method == 'POST':
        Product.objects.create(
            name = request.POST['name'],
            description = request.POST['description'],
            price = request.POST['price']
        )

    return redirect('/products')

# update: Process information from the edit form and update the particular product
def update(request, id):
    pass

# destroy: Remove a product
def destroy(request, id):
    pass
