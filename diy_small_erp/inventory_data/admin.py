from django.contrib import admin
from .forms import StockCreateForm
from simple_history.admin import SimpleHistoryAdmin
from .models import Stock, StockHistory


class StockCreateAdmin(admin.ModelAdmin):
   list_display = ['ean', 'brand', 'item_name', 'quantity']
   form = StockCreateForm
   list_filter = ['brand']
   search_fields = ['brand', 'item_name']

class StockCreateHistoryAdmin(admin.ModelAdmin):
   list_display = ['ean', 'brand', 'item_name', 'receive_quantity', 'supplier', 'issue_quantity', 'issue_to']
   list_filter = ['brand']
   search_fields = ['brand', 'item_name', 'supplier', 'issue_to']

admin.site.register(Stock, StockCreateAdmin)
admin.site.register(StockHistory, StockCreateHistoryAdmin)
