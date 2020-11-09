from django.urls import path
from . import views
from .views import StockListView, StockDetailView, SearchResultsView, StockDeleteView, HistoryStockListView

urlpatterns = [
	path('', views.home, name='home'),
	path('inventory-store-a/', StockListView.as_view(), name='inventory-store-a'),
	path('inventory-store-a/<slug:slug>/', StockDetailView.as_view(), name='inventory-store-a-detail'),
	path('add-items-store-a/', views.add_items, name='add-items-store-a'),
	path('items-store-a/<slug:slug>/delete', StockDeleteView.as_view(), name='deletestock'),
	path('items-store-a/<slug:slug>/edit', views.edit_item, name='editstock'),
	path('items-store-a/<slug:slug>/receive', views.receive_items, name='receive'),
	path('items-store-a/<slug:slug>/selling', views.selling_items, name='selling'),
	path('items-history-store-a/', HistoryStockListView.as_view(), name='items-history'),
	path('search-store-a/', SearchResultsView.as_view(), name='search_results'),
	# path('search-history-store-a/', SearchHistoryResultsView.as_view(), name='search_history_results'),
	]