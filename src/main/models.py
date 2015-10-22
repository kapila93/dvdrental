from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class category(models.Model):
	name = models.CharField(max_length=25, null=False)
	last_update = models.DateTimeField(auto_now=True)
	
	class Meta:
		verbose_name = _('category')
		verbose_name_plural = _('categories')
	
	def __unicode__(self):
		return u'%s' % (self.name)

class language(models.Model):
	name = models.CharField(max_length=20, null=False)
	last_update = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return u'%s' % (self.name)	

class film(models.Model):
	title = models.CharField(max_length=255, null=False)
	description = models.TextField()
	release_year = models.IntegerField()
	language_id = models.ForeignKey('language')
	rental_duration = models.IntegerField()
	rental_rate = models.FloatField()
	length = models.IntegerField()
	replacement_cost = models.FloatField()
	rating = models.CharField(max_length=10)
	last_update = models.DateTimeField(auto_now=True)
	special_features = models.TextField()
	fulltext = models.TextField()

	def __unicode__(self):
		return u'%s' % (self.title)

class film_category(models.Model):
	film_id = models.ForeignKey('film')
	category_id = models.ForeignKey('category')
	last_update = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = _('film category')
		verbose_name_plural = _('film categories')

	def __unicode__(self):
		return u'%s' % (self.film_id)

class actor(models.Model):
	first_name = models.CharField(max_length=45, null=False)
	last_name = models.CharField(max_length=45, null=False)
	last_update = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)

class film_actor(models.Model):
	actor_id = models.ForeignKey('actor')
	film_id = models.ForeignKey('film')
	last_update = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = _('film actor')
		verbose_name_plural = _('film actors')

	def __unicode__(self):
		return u'%s | %s' % (self.actor_id, self.film_id)

class country(models.Model):
	country = models.CharField(max_length=50, null=False)
	last_update = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = _('country')
		verbose_name_plural = _('countries')

	def __unicode__(self):
		return u'%s' % (self.country)

class city(models.Model):
	city = models.CharField(max_length=50, null=False)
	country_id = models.ForeignKey('country')
	last_update = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = _('city')
		verbose_name_plural = _('cities')

	def __unicode__(self):
		return u'%s' % (self.city)

class address(models.Model):
	address = models.CharField(max_length=50, null=False)
	address2 = models.CharField(max_length=50, null=True)
	district = models.CharField(max_length=20)
	city_id = models.ForeignKey(city)
	postal_code = models.CharField(max_length=10)
	phone = models.CharField(max_length=20, null=True)
	last_update = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = _('address')
		verbose_name_plural = _('addresses')

	def __unicode__(self):
		return u'%s, %s, %s' % (self.address, self.city_id, self.postal_code)

class store(models.Model):
	manager_staff_id = models.ForeignKey('staff')
	address_id = models.ForeignKey('address')
	last_update = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return u'%s' % (self.address_id)

class staff(models.Model):
	first_name = models.CharField(max_length=45, null=False)
	last_name = models.CharField(max_length=45, null=False)
	address_id = models.ForeignKey('address')
	email = models.CharField(max_length=50, null=False)
	store_id = models.ForeignKey('store')
	active = models.BooleanField()
	username = models.CharField(max_length=16)
	password = models.CharField(max_length=40)
	last_update = models.DateTimeField(auto_now=True)
	picture = models.CharField(max_length=50, null=True)

	class Meta:
		verbose_name = _('staff')
		verbose_name_plural = _('staff')

	def __unicode__(self):
		return u'%s, %s' % (self.last_name, self.first_name)

class inventory(models.Model):
	film_id = models.ForeignKey('film')
	store_id = models.ForeignKey('store')
	last_update = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = _('inventory')
		verbose_name_plural = _('inventories')

class rental(models.Model):
	rental_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	inventory_id = models.ForeignKey('inventory') 
	customer_id = models.ForeignKey('customer')
	return_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
	staff_id = models.ForeignKey('staff')
	last_update = models.DateTimeField(auto_now=True)

class payment(models.Model):
	customer_id = models.ForeignKey('customer')
	staff_id = models.ForeignKey('staff')
	rental_id = models.ForeignKey('rental')
	amount = models.FloatField()
	payment_date = models.DateTimeField(auto_now=False, auto_now_add=False)

class customer(models.Model):
	store_id = models.ForeignKey('store')
	first_name = models.CharField(max_length=45, null=False)
	last_name = models.CharField(max_length=45, null=False)
	email = models.CharField(max_length=50)
	address_id = models.ForeignKey('address')
	activebool = models.BooleanField()
	create_date = models.DateField(auto_now=False, auto_now_add=False)
	last_update = models.DateTimeField(auto_now=True)
	active = models.IntegerField()

	def __unicode__(self):
		return u'%s %s' % (self.last_name, self.first_name)