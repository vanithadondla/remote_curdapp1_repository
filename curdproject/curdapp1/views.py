from django.shortcuts import render
from .models import ProductData
from .forms import ProductInsertForm,ProductUpdateForm,ProductDeleteForm
from django.http.response import HttpResponse
def home(request):
    return render(request,'product_home.html')
def product_insert_view(request):
    if request.method=="POST":
        iform=ProductInsertForm(request.POST)
        if iform.is_valid():
            product_id=request.POST.get('product_id','')
            product_name=request.POST.get('product_name', '')
            product_cost=request.POST.get('product_cost', '')
            product_color=request.POST.get('product_color', '')
            product_class=request.POST.get('product_class', '')
            customer_name=request.POST.get('customer_name', '')
            customer_mobile=request.POST.get('customer_mobile', '')
            customer_email=request.POST.get('customer_email','')
            data=ProductData(
                product_id=product_id,
                product_name=product_name,
                product_cost=product_cost,
                product_color=product_color,
                product_class=product_class,
                customer_name=customer_name,
                customer_mobile=customer_mobile,
                customer_email=customer_email,
            )
            data.save()
            iform=ProductInsertForm()
            return render(request,'product_insert.html',{'iform':iform})
    else:
        iform = ProductInsertForm()
        return render(request, 'product_insert.html',{'iform':iform})

def product_retrieve_view(request):
    products_data=ProductData.objects.all()
    return render(request,'product_retrieve.html',{'pdata':products_data})

def product_update_view(request):
    if request.method=="POST":
        uform=ProductUpdateForm(request.POST)
        if uform.is_valid():
            product_id=request.POST.get('product_id','')
            product_cost=request.POST.get('product_cost','')
            pdata=ProductData.objects.filter(product_id=product_id)
            if not pdata:
                return HttpResponse('product is not available')
            else:
                pdata.update(product_cost=product_cost)
                uform=ProductUpdateForm()
                return render(request,'product_update.html',{'uform':uform})
        else:
            return HttpResponse('Invalid Form')
    else:
        uform=ProductUpdateForm()
        return render(request,'product_update.html',{'uform':uform})
def product_delete_view(request):
    if request.method=="POST":
        dform=ProductDeleteForm(request.POST)
        if dform.is_valid():
            product_id=request.POST.get('product_id','')
            pdata=ProductData.objects.filter(product_id=product_id)
            if not pdata:
                return HttpResponse('product is not available')
            else:
                pdata.delete()
                dform=ProductDeleteForm()
                return render(request,'product_delete.html',{'dform':dform})
        else:
            return HttpResponse('Invalid Form')
    else:
        dform=ProductDeleteForm()
        return render(request,'product_delete.html',{'dform':dform})
















