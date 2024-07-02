from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Category)

# Define ProductAdmin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'digital', 'description', 'stock')
    list_filter = ('category', 'digital')
    search_fields = ('name', 'description')

    def get_fieldsets(self, request, obj=None):
        if obj and obj.digital:
            return [
                (None, {'fields': ('name', 'price', 'description', 'image', 'digital', 'category')}),
            ]
        else:
            return [
                (None, {'fields': ('name', 'price', 'description', 'image', 'digital', 'category', 'stock')}),
            ]

admin.site.register(Product, ProductAdmin)
