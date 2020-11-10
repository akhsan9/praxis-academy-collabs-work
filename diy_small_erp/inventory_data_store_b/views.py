from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from .models import StockStoreB, StockHistoryStoreB
from .forms import StockCreateFormStoreB, StockEditFormStoreB, ReceiveFormStoreB, SellingFormStoreB
from django.views.generic import ListView, DetailView, DeleteView
from django.db.models import Q
from django.contrib import messages

#eng: adding a new item
#ind: view untuk menambahkan item baru
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

#eng: edit an item
#ind: edit produk
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

#eng: delete an object
#ind: menghapus sebuah object
class StockDeleteView(DeleteView): 
	model = StockStoreB
	template_name =	'inventory_data_store_b/stock_confirm_delete.html'
	success_url ="/"

#eng: list all objects
#ind: menampilkan semua object
class StockListView(ListView):
	model = StockStoreB
	template_name = 'inventory_data_store_b/stock_list.html'
	context_object_name ='inventory_store_b'
	# ordering = ['last_updated']

#eng: see detail of an object
#ind: melihat detail sebuah object
class StockDetailView(DetailView):
	model = StockStoreB
	template_name = 'inventory_data_store_b/stock_list_detail.html'

#eng: showing search result
#ind: melihat result
class SearchResultsView(ListView):
	model = StockStoreB
	template_name = 'inventory_data_store_b/search_result.html'
	#eng: function for get query for search result
	#ind: function untuk mendapatkan query dan menampilkan di halaman search result
	def get_queryset(self): 
		query = self.request.GET.get('q')
		object_list_store_b = StockStoreB.objects.filter(
			Q(brand__icontains=query) | Q(item_name__icontains=query)
		)
		return object_list_store_b

#eng: for adding more stock to the stock that has already before
#ind: untuk menambahkan jumlah barang ke dalam stock yang sudah ada
def receive_items(request, slug):
	queryset = StockStoreB.objects.get(slug=slug)
	form = ReceiveFormStoreB(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity += instance.receive_quantity
		instance.save()
		#eng: write all received history
		#ind: mencatat semua history penerimaan barang
		receive_history = StockHistoryStoreB(
			slug = instance.slug,
			ean = instance.ean,
			last_updated = instance.last_updated,
			brand = instance.brand,
			item_name = instance.item_name,
			receive_invoice = instance.receive_invoice,
			quantity = instance.quantity,
			receive_quantity = instance.receive_quantity,
			receive_by = instance.receive_by,
			supplier = instance.supplier
			)
		receive_history.save()
		messages.success(request, "Received " + str(instance.receive_quantity) + ". " + str(instance.quantity) + " " + str(instance.item_name)+"s now in Store")
		return HttpResponseRedirect(instance.get_product_url())
	context = {
			"title": 'Receive ' + str(queryset.item_name),
			"instance": queryset,
			"form": form,
			"username": 'Receive By: ' + str(request.user),
		}
	return render(request, "inventory_data_store_b/add_items.html", context)

#eng: for selling already prodcut
#ind: untuk menghapus
def selling_items(request, slug):
	queryset = StockStoreB.objects.get(slug=slug)
	form = SellingFormStoreB(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity -= instance.issue_quantity
		instance.issue_by = str(request.user)
		messages.success(request, "Sold " +  str(instance.issue_quantity) + " items. " + str(instance.quantity) + " " + str(instance.item_name) + "s now left in Store")
		instance.save()
		issue_history = StockHistoryStoreB(
			slug = instance.slug,
			ean = instance.ean,
			last_updated = instance.last_updated,
			brand = instance.brand,
			item_name = instance.item_name,
			quantity = instance.quantity,
			issue_quantity = instance.issue_quantity,
			issue_invoice = instance.issue_invoice,
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
	return render(request, "inventory_data_store_b/add_items.html", context)

#eng: showing selling&receiving a product
#ind: menampilkan history jual&beli sebuah product
class HistoryStockListView(ListView):
	model = StockHistoryStoreB
	template_name = 'inventory_data_store_b/history.html'
	context_object_name = 'queryset_history'
	ordering = ['-last_updated']

#eng: showing search result
#ind: melihat result
class HistorySearchResultsView(ListView):
	model = StockHistoryStoreB
	template_name = 'inventory_data_store_b/history_search_result.html'
	def get_queryset(self):
		query = self.request.GET.get('q)')
		object_list = StockHistoryStoreB.object.filter(
			Q(supplier__icontains=query) | Q(issue_to__icontains=query)
		)
		return object_list

def reorder_level(request, slug):
	reorder = StockHistoryStoreB.object.get(slug=slug)
	form = ReorderLevelForm(request.POST or None,instance=reorder)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Reorder level for " + str(instance.item_name) + " is update to " + str(instance.reorder_level))
		return redirect("inventory-store-b")
	context = {
			"instance": reorder,
			"form": form,
		}
	return render(request, "inventory_data_store_b/add_item.html", context)
