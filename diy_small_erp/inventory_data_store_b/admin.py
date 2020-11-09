from django.contrib import admin
from .forms import StockCreateFormStoreB
from .models import StockStoreB


class StockCreateFormStoreB(admin.ModelAdmin):
   list_display = ['ean', 'brand', 'item_name', 'quantity']
   form = StockCreateFormStoreB
   list_filter = ['brand']
   search_fields = ['brand', 'item_name']

admin.site.register(StockStoreB, StockCreateFormStoreB)

