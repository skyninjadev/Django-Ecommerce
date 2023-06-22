from django.contrib import admin
from .models import Product, Order, Contact

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Contact)

admin.site.site_header = 'RushX Administration'

