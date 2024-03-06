from django.contrib import admin
from .models import Product, Attr, ProductAttr, UniqueProduct


class ProductAdmin(admin.ModelAdmin):
    pass


class AttrAdmin(admin.ModelAdmin):
    pass


class ProductAttrAdmin(admin.ModelAdmin):
    pass


class UniqueProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Attr, AttrAdmin)
admin.site.register(ProductAttr, ProductAttrAdmin)
admin.site.register(UniqueProduct, UniqueProductAdmin)
