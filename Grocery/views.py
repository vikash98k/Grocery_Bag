from django.shortcuts import render,redirect
from .models import Gro

def index(request):
	items = Gro.objects.all()
	context = {'items':items}
	return render(request,'Grocery/index.html',context)

def create(request):
	if(request.method=='POST'):
		item=Gro(item_name=request.POST['item_name'],item_quantity=request.POST['item_quantity'],item_status=request.POST['item_status'])
		item.save()

	return render(request,'Grocery/create.html')


def edit(request, id):
    items = Gro.objects.get(id=id)
    context = {'items': items}
    return render(request, 'Grocery/edit.html', context)

def update(request, id):
    item = Gro.objects.get(id=id)
    item.item_name = request.POST['item_name']
    item.item_quantity = request.POST['item_quantity']
    item.item_status = request.POST['item_status']
    item.save()
    return redirect('/')

def delete(request, id):
    item = Gro.objects.get(id=id)
    item.delete()
    return redirect('/')