from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Stock(models.Model):
#items detail	
	slug = models.SlugField(null=True, unique=True, blank=False, verbose_name="URL Product") 
	brand = models.CharField(max_length=50, blank=True, null=True, verbose_name='Brand')
	ean = models.CharField(max_length=50, blank=True, null=True, unique=True, verbose_name='Product ID')
	item_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Product Name')
	quantity = models.IntegerField(default='0', blank=True, null=True, verbose_name='Total Quantity')
	
#receive stock
	supplier = models.CharField(max_length=50, blank=True, null=True, verbose_name="Supplier") 
	receive_invoice = models.CharField(max_length=50, blank=True, null=True, verbose_name="No. Invoice")
	receive_quantity = models.IntegerField(default='0', blank=True, null=True, verbose_name='Received Quantity')
	receive_by = models.CharField(max_length=50, blank=True, null=True, verbose_name="Warehouse Admin")

#selling stock
	issue_to = models.CharField(max_length=50, blank=True, null=True, verbose_name='Buyer')
	issue_invoice = models.CharField(max_length=50, blank=True, null=True, verbose_name="Supplier")
	issue_quantity = models.IntegerField(default='0', blank=True, null=True, verbose_name="Sell Out Quantity")
	issue_by = models.CharField(max_length=50, blank=True, null=True, verbose_name='Warehouse Admin')

#extra
	reorder_level = models.IntegerField(default='0', blank=True, null=True)
	date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)


	class Meta:
		verbose_name_plural = "Stock Store A"

	def __str__(self):
		return self.item_name

	def get_product_url(self):
			return reverse('inventory-store-a-detail', kwargs={'slug': self.slug}) #get slug url 
	
	def get_edit_url(self):
			return reverse('editstock', kwargs={'slug': self.slug}) #get slug url 

	def get_delete_url(self):
			return reverse('deletestock', kwargs={'slug': self.slug}) #get slug url 

	def get_receive_url(self):
			return reverse('receive', kwargs={'slug': self.slug}) #get slug url 

	def get_selling_url(self):
			return reverse('selling', kwargs={'slug': self.slug}) #get slug url 

class StockHistory(models.Model):
#items detail
	slug = models.SlugField(blank=True, null=True, verbose_name="URL Product") 
	brand = models.CharField(max_length=50, blank=True, null=True, verbose_name='Brand')
	ean = models.CharField(max_length=50, blank=True, null=True, verbose_name='Product ID')
	item_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Product Name')
	quantity = models.IntegerField(default='0', blank=True, null=True, verbose_name='Total Quantity')
	
#receive stock
	supplier = models.CharField(max_length=50, blank=True, null=True, verbose_name="Supplier") 
	receive_invoice = models.CharField(max_length=50, blank=True, null=True, verbose_name="No. Invoice")
	receive_quantity = models.IntegerField(default='0', blank=True, null=True, verbose_name='Received Quantity')
	receive_by = models.CharField(max_length=50, blank=True, null=True, verbose_name="Warehouse Admin")


#selling stock
	issue_to = models.CharField(max_length=50, blank=True, null=True, verbose_name='Buyer')
	issue_invoice = models.CharField(max_length=50, blank=True, null=True, verbose_name="Invoice Sell Out")
	issue_quantity = models.IntegerField(default='0', blank=True, null=True, verbose_name="Sell Out Quantity")
	issue_by = models.CharField(max_length=50, blank=True, null=True, verbose_name='Warehouse Admin')

#extra
	reorder_level = models.IntegerField(default='0', blank=True, null=True)
	date_added = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)

	class Meta:
		verbose_name_plural = "Stock History Store A"

	def __str__(self):
		return self.item_name

