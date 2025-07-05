from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Item

# Create your views here.
#CRUD

#HOME view
def home(request):
    return render(request,'invApp/home.html')

#CREATE view
def create_product(request):
    form= ProductForm()
    if request.method=='POST':
        form= ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request,'invApp/product_form.html',{'form':form})

#READ view
def product_list_view(request):
    products= Item.objects.all()
    return render(request,'invApp/product_list.html',{'products':products})

#UPDATE view
def update_product(request,product_id):
    product=Item.objects.get(product_id=product_id)
    form= ProductForm()
    if request.method=='POST':
        form=ProductForm(request.POST,instance= product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    
    return render(request,'invApp/product_form.html',{'form':form})
            

#DELETE view
def delete_product(request,product_id):
    product= Item.objects.get(product_id=product_id)
    if request.method=='POST':
        product.delete()
        return redirect('product_list')
    return render(request,'invApp/product_confirm_delete.html',{'product':product})
