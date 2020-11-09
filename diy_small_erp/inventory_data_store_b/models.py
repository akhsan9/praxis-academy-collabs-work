from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse


class StockStoreB(models.Model):
#items detail	
	slug = models.SlugField(null=True, unique=True, blank=False, verbose_name="URL Product") 
	brand = models.CharField(max_length=50, blank=True, null=True, verbose_name='Brand')
	ean = models.CharField(max_length=50, blank=True, null=True, unique=True, verbose_name='Product ID')
	item_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Product Name')
	quantity = models.IntegerField(default='0', blank=True, null=True, verbose_name='Total Quantity')
	
#receive stock
	receive_quantity = models.IntegerField(default='0', blank=True, null=True, verbose_name='Received Quantity')
	receive_by = models.CharField(max_length=50, blank=True, null=True, verbose_name="Warehouse Admin")
	supplier = models.CharField(max_length=50, blank=True, null=True, verbose_name="Supplier") 

#selling stock
	issue_quantity = models.IntegerField(default='0', blank=True, null=True, verbose_name="Sell Out Quantity")
	issue_by = models.CharField(max_length=50, blank=True, null=True, verbose_name='Warehouse Admin')
	issue_to = models.CharField(max_length=50, blank=True, null=True, verbose_name='Buyer')
	created_by = models.CharField(max_length=50, blank=True, null=True)

#extra
	reorder_level = models.IntegerField(default='0', blank=True, null=True)
	date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	class Meta:
		verbose_name_plural = "Stock Store B"

	def __str__(self):
		return self.item_name

	def get_product_url(self):
			return reverse('inventory-store-b-detail', kwargs={'slug': self.slug}) #get slug url 
	
	def get_edit_url(self):
			return reverse('editstockstoreb', kwargs={'slug': self.slug}) #get slug url 

	def get_delete_url(self):
			return reverse('deletestockstoreb', kwargs={'slug': self.slug}) #get slug url 

	def get_receive_url(self):
			return reverse('receivestoreb', kwargs={'slug': self.slug}) #get slug url 

	def get_selling_url(self):
			return reverse('sellingstoreb', kwargs={'slug': self.slug}) #get slug url 





