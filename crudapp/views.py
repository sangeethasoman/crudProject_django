from django.shortcuts import redirect, render
from crudapp.models import ProductDetails

# Create your views here.
#Load addProduct.html Page........
def addProduct(request):
    return render(request,'addProduct.html')

#Enter Product Details...
def add_product_details(request):
    if request.method=='POST':
        pname=request.POST['product_name']
        des=request.POST['description']
        qty=request.POST['quantity']
        price=request.POST['price']
        
        product=ProductDetails(Product_name=pname,
                               description=des,
                               quantity=qty,
                               price=price)

        product.save()
        print("hii")
        return redirect('show_products')
         
         #Show Products Detsils...
def show_products(request):
    products=ProductDetails.objects.all()
    return render(request,'showPimg.html',{'product':products})

#Load Edit Page....
def editpage(request,pk):
    products=ProductDetails.objects.get(id=pk) #.....select * from tablename where id = 7;
    return render(request,'edit.html',{'products':products})

#Editing..
def edit_product_details(request,pk):
    if request.method=='POST':
        products = ProductDetails.objects.get(id=pk)
        products.Product_name = request.POST.get('product_name')
        products.description = request.POST.get('description')
        products.quantity = request.POST.get('quantity')
        products.price = request.POST.get('price')
        products.save()
        return redirect('show_products')
    return render(request, 'edit.html',)

#Load delete Page...
def deletepage(request,pk):
    products=ProductDetails.objects.get(id=pk)
    return render(request,'delete.html',{'products':products})

#Deleting Product Element..
def delete_product(request,pk):
    products=ProductDetails.objects.get(id=pk)
    products.delete()
    return redirect('show_products')