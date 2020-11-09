from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from .models import StockStoreB
from .forms import StockCreateFormStoreB, StockEditFormStoreB, ReceiveFormStoreB, SellingFormStoreB
from django.views.generic import ListView, DetailView, DeleteView
from django.db.models import Q
from django.contrib import messages

def add_items(request):
	if request.method == "POST":
		form = StockCreateFormStoreB(request.POST)
		if form.is_valid():
			createstock = form.save()
			createstock.save()
			return redirect('inventory-store-b')
	else:
		form = StockCreateFormStoreB()
	return render(request, 'inventory_data_store_b/add_items.html', {'form': form})

def edit_item(request, slug):
		stock = get_object_or_404(StockStoreB, slug=slug)
		if request.method == "POST":
				form = StockEditFormStoreB(request.POST, instance=stock)
				if form.is_valid():
						stock = form.save(commit=False)
						stock.save()
						return redirect('inventory-store-b-detail', slug=stock.slug)
		else:
				form = StockEditFormStoreB(instance=stock)
		return render(request, 'inventory_data_store_b/edit_items.html', {'form': form})	

class StockDeleteView(DeleteView): 
	model = StockStoreB
	template_name =	'inventory_data_store_b/stock_confirm_delete.html'
	success_url ="/"
	
class StockListView(ListView):
	model = StockStoreB
	template_name = 'inventory_data_store_b/stock_list.html'
	context_object_name ='inventory_store_b'
	# ordering = ['last_updated']

class StockDetailView(DetailView):
	model = StockStoreB
	template_name = 'inventory_data_store_b/stock_list_detail.html'

class SearchResultsView(ListView):
	model = StockStoreB
	template_name = 'inventory_data/search_result.html'

	def get_queryset(self): 
		query = self.request.GET.get('q')
		object_list_store_b = StockStoreB.objects.filter(
			Q(brand__icontains=query) | Q(item_name__icontains=query)
		)
		return object_list_store_b

def receive_items(request, slug):
	queryset = StockStoreB.objects.get(slug=slug)
	form = ReceiveFormStoreB(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity += instance.receive_quantity
		instance.save()
		messages.success(request, "Received " + str(instance.receive_quantity) + ". " + str(instance.quantity) + " " + str(instance.item_name)+"s now in Store")
		return HttpResponseRedirect(instance.get_product_url())
	context = {
			"title": 'Receive ' + str(queryset.item_name),
			"instance": queryset,
			"form": form,
			"username": 'Receive By: ' + str(request.user),
		}
	return render(request, "inventory_data_store_b/add_items.html", context)

def selling_items(request, slug):
	queryset = StockStoreB.objects.get(slug=slug)
	form = SellingFormStoreB(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity -= instance.issue_quantity
		instance.issue_by = str(request.user)
		messages.success(request, "Sold " +  str(instance.issue_quantity) + " items. " + str(instance.quantity) + " " + str(instance.item_name) + "s now left in Store")
		instance.save()
		return HttpResponseRedirect(instance.get_product_url())

	context = {
		"title": 'Issue ' + str(queryset.item_name),
		"queryset": queryset,
		"form": form,
		"username": 'Issue By: ' + str(request.user),
	}
	return render(request, "inventory_data_store_b/add_items.html", context)