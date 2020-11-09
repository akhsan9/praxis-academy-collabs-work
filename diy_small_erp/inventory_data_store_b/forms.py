from django import forms
from .models import StockStoreB


class StockCreateFormStoreB(forms.ModelForm):
	class Meta:
		model = StockStoreB
		fields = ['slug','brand', 'ean', 'item_name']

	def clean_brand_store_b(self):
		brand = self.cleaned_data.get('brand')
		if not brand:
			raise forms.ValidationError('This field is required')
		return brand

	def clean_item_name_store_b(self):
		item_name = self.cleaned_data.get('item_name')
		if not item_name:
			raise forms.ValidationError('This field is required')
		return item_name

class StockEditFormStoreB(forms.ModelForm):
	class Meta:
		model = StockStoreB
		fields = ['slug','brand', 'ean', 'item_name']

class ReceiveFormStoreB(forms.ModelForm):
	class Meta:
		model = StockStoreB
		fields = ['receive_quantity', 'receive_by', 'supplier']

class SellingFormStoreB(forms.ModelForm):
	class Meta:
		model = StockStoreB
		fields = ['issue_quantity', 'issue_to']