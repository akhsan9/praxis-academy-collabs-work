from django.urls import path
from . import views
from .views import StockListView, StockDetailView, SearchResultsView, StockDeleteView, HistoryStockListView, HistorySearchResultsView

urlpatterns = [
	path('inventory-store-b/', StockListView.as_view(), name='inventory-store-b'),
	path('inventory-store-b/<slug:slug>/', StockDetailView.as_view(), name='inventory-store-b-detail'),
	path('add-items-store-b/', views.add_items, name='add-items-store-b'),
	path('items-store-b/<slug:slug>/delete', StockDeleteView.as_view(), name='deletestockstoreb'),
	path('items-store-b/<slug:slug>/edit', views.edit_item, name='editstockstoreb'),
	path('items-store-b/<slug:slug>/receive', views.receive_items, name='receivestoreb'),
	path('items-store-b/<slug:slug>/selling', views.selling_items, name='sellingstoreb'),
	path('items-history-store-b/', HistoryStockListView.as_view(), name='items-history-store-b'),
	path('search-store-b/', SearchResultsView.as_view(), name='search_results_store_b'),
	path('search-history-store-b/', HistorySearchResultsView.as_view(), name='search_history_results_store_b'),
	path('reorder_level/<slug:slug>/', views.reorder_level, name="reorder_level_store_b"),
	]