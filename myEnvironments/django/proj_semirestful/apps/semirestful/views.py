from django.shortcuts import render, redirect
from .models import Product

# Display all products
def index(request):
    return render(request, 'semirestful/index.html', { "products" :  Product.objects.all() } )

# Display a particular product
def show(request, id):
    return render(request, 'semirestful/show_product.html', { "product" :  Product.objects.get(id = id) } )

# Display a form to create a new product
def new(request):
    return render(request, 'semirestful/new_product.html')

# Display a form to update a product
def edit(request, id):
    return render(request, 'semirestful/edit_product.html', { "product" :  Product.objects.get(id = id) } )

# Process information to create a new product
def create(request):
    if request.method == 'POST':
        Product.objects.create(
            name = request.POST['name'],
            description = request.POST['description'],
            price = request.POST['price']
        )

    return redirect('/products')

# Process information from the edit form and update the particular product
def update(request, id):
    if request.method == 'POST':
        product = Product.objects.get(id = id)

        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']

        product.save()

    return redirect('/products')

# Remove a product
def destroy(request, id):
    Product.objects.get(id = id).delete()
    return redirect('/products')
