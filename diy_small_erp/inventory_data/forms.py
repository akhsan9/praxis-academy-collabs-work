from django import forms
from .models import Stock


class StockCreateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['slug','brand', 'ean', 'item_name']

	def clean_category(self):
		brand = self.cleaned_data.get('brand')
		if not brand:
			raise forms.ValidationError('This field is required')
		return brand

	def clean_item_name(self):
		item_name = self.cleaned_data.get('item_name')
		if not item_name:
			raise forms.ValidationError('This field is required')
		return item_name

class StockEditForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['slug','brand', 'ean', 'item_name']

class ReceiveForm(forms.ModelForm):
	class Meta:
		model = Stock
<<<<<<< HEAD
		fields = ['receive_invoice', 'receive_quantity', 'receive_by', 'supplier']
=======
		fields = ['supplier', 'receive_invoice' ,'receive_quantity', 'receive_by']
>>>>>>> master

class SellingForm(forms.ModelForm):
	class Meta:
		model = Stock
<<<<<<< HEAD
		fields = ['issue_invoice','issue_quantity', 'issue_by', 'issue_to']
=======
		fields = ['issue_to', 'issue_invoice', 'issue_quantity', 'issue_by']
>>>>>>> master
