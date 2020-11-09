from django.contrib import admin
from .forms import StockCreateForm
from simple_history.admin import SimpleHistoryAdmin
from .models import Stock, StockHistory


class StockCreateAdmin(admin.ModelAdmin):
   list_display = ['ean', 'brand', 'item_name', 'quantity']
   form = StockCreateForm
   list_filter = ['brand']
   search_fields = ['brand', 'item_name']


# class StockCreateAdminStoreB(admin.ModelAdmin):
#    list_display = ['ean', 'brand', 'item_name', 'quantity']
#    form = StockCreateFormStoreB
#    list_filter = ['brand']
#    search_fields = ['brand', 'item_name']

# class HistoryAdmin(SimpleHistoryAdmin):
#     list_display = ['receive_quantity', 'receive_by', 'supplier']

# admin.site.register(Stock, StockCreateAdmin)
admin.site.register(Stock, StockCreateAdmin)
admin.site.register(StockHistory)
# admin.site.register(StockStoreB, StockCreateFormStoreB)

