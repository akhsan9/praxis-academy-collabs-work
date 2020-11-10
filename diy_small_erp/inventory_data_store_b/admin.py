from django.contrib import admin
from .forms import StockCreateFormStoreB
from simple_history.admin import SimpleHistoryAdmin
from .models import StockStoreB, StockHistoryStoreB


class StockCreateFormStoreB(admin.ModelAdmin):
   list_display = ['ean', 'brand', 'item_name', 'quantity']
   form = StockCreateFormStoreB
   list_filter = ['brand']
   search_fields = ['brand', 'item_name']

class StockCreateHistoryFormStoreB(admin.ModelAdmin):
   list_display = ['ean', 'brand', 'item_name', 'receive_quantity', 'supplier', 'issue_quantity', 'issue_to']
   list_filter = ['brand']
   search_fields = ['brand', 'item_name', 'supplier', 'issue_to']

admin.site.register(StockStoreB, StockCreateFormStoreB)
admin.site.register(StockHistoryStoreB, StockCreateHistoryFormStoreB)

