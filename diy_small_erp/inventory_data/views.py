from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from .models import Stock, StockHistory
from .forms import StockCreateForm, StockEditForm, ReceiveForm, SellingForm
from django.views.generic import ListView, DetailView, DeleteView
from django.db.models import Q
from django.contrib import messages


#homepage view
def home(request):
	title = 'Stock management home.'
	context = {
	"title": title,
	}
	return render(request, "inventory_data/home.html", context)

#eng: adding a new item
#ind: view untuk menambahkan item baru
def add_items(request):
	if request.method == "POST":
		form = StockCreateForm(request.POST)
		if form.is_valid():
			createstock = form.save()
			createstock.save()
			return redirect('inventory-store-a')
	else:
		form = StockCreateForm()
	return render(request, 'inventory_data/add_items.html', {'form': form})

#eng: edit an item
#ind: edit produk
def edit_item(request, slug):
		stock = get_object_or_404(Stock, slug=slug)
		if request.method == "POST":
				form = StockEditForm(request.POST, instance=stock)
				if form.is_valid():
						stock = form.save(commit=False)
						stock.save()
						return redirect('inventory-store-a-detail', slug=stock.slug)
		else:
				form = StockEditForm(instance=stock)
		return render(request, 'inventory_data/edit_items.html', {'form': form})	

#eng: delete an object
#ind: menghapus sebuah object
class StockDeleteView(DeleteView): 
	model = Stock
	template_name =	'inventory_data/stock_confirm_delete.html'
	success_url ="/"

#eng: list all objects
#ind: menampilkan semua object	
class StockListView(ListView):
	model = Stock
	template_name = 'inventory_data/stock_list.html'
	context_object_name ='inventory'
	ordering = ['-last_updated']

#eng: see detail of an object
#ind: melihat detail sebuah object
class StockDetailView(DetailView):
	model = Stock
	template_name = 'inventory_data/stock_list_detail.html'

#eng: showing search result
#ind: melihat result
class SearchResultsView(ListView):
	model = Stock
	template_name = 'inventory_data/search_result.html'
	#eng: function for get query for search result
	#ind: function untuk mendapatkan query dan menampilkan di halaman search result
	def get_queryset(self): 
		query = self.request.GET.get('q')
		object_list = Stock.objects.filter(
			Q(brand__icontains=query) | Q(item_name__icontains=query)
		)
		return object_list

#eng: for adding more stock to the stock that has already before
#ind: untuk menambahkan jumlah barang ke dalam stock yang sudah ada
def receive_items(request, slug):
	queryset = Stock.objects.get(slug=slug)
	form = ReceiveForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity += instance.receive_quantity
		instance.save()
		#eng: write all received history
		#ind: mencatat semua history penerimaan barang
		receive_history = StockHistory(
			slug = instance.slug,
			ean = instance.ean,
			last_updated = instance.last_updated,
			brand = instance.brand,
			item_name = instance.item_name, 
			quantity = instance.quantity,
			receive_quantity = instance.receive_quantity,
			receive_by = instance.receive_by,
			supplier = instance.supplier
			)
		receive_history.save()		
		messages.success(request, "Received " + str(instance.quantity) + " " + str(instance.item_name)+"s now in Store")
		return HttpResponseRedirect(instance.get_product_url())
	context = {
			"title": 'Receive ' + str(queryset.item_name),
			"instance": queryset,
			"form": form,
			"username": 'Receive By: ' + str(request.user),
		}
	return render(request, "inventory_data/add_items.html", context)

#eng: for selling already prodcut
#ind: untuk menghapus 
def selling_items(request, slug):
	queryset = Stock.objects.get(slug=slug)
	form = SellingForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity -= instance.issue_quantity
		instance.issue_by = str(request.user)
		messages.success(request, "Sold " + str(instance.issue_quantity) + ". " + str(instance.quantity) + " " + str(instance.item_name) + "s now left in Store")
		instance.save()
		issue_history = StockHistory(
			slug = instance.slug,
			ean = instance.ean, 
			last_updated = instance.last_updated,
			brand = instance.brand,
			item_name = instance.item_name, 
			quantity = instance.quantity,
			issue_quantity = instance.issue_quantity, 
			issue_by = instance.issue_by,
			issue_to = instance.issue_to
			)
		issue_history.save()
		return HttpResponseRedirect(instance.get_product_url())
	context = {
		"title": 'Issue ' + str(queryset.item_name),
		"queryset": queryset,
		"form": form,
		"username": 'Issue By: ' + str(request.user),
	}
	return render(request, "inventory_data/add_items.html", context)

#eng: showing selling&receiving a product
#ind: menampilkan history jual&beli sebuah product
class HistoryStockListView(ListView):
	model = StockHistory
	template_name = 'inventory_data/history.html'
	context_object_name ='queryset_history'
	ordering = ['-last_updated']

#eng: showing search result
#ind: melihat result
class HistorySearchResultsView(ListView):
	model = StockHistory
	template_name = 'inventory_data/history_search_result.html'
	def get_queryset(self): 
		query = self.request.GET.get('q')
		object_list = StockHistory.objects.filter(
			Q(supplier__icontains=query) | Q(issue_to__icontains=query)
		)
		return object_list