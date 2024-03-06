from django.db import models

'''
Создаем кастомный FK.
'''


class CustomForeignKey(models.ForeignKey):
    def __init__(self, to, on_delete, **kwargs):
        self.related_accessor_class = CustomRelatedManager
        super().__init__(to, on_delete, **kwargs)

    def contribute_to_related_class(self, cls, related):
        super().contribute_to_related_class(cls, related)
        setattr(cls, self.name, self.related_accessor_class(self))


class CustomRelatedManager(models.Manager):
    def __init__(self, field):
        super().__init__()
        self.field = field

    def all(self):
        return super().all()

    def generate(self, product_instance):
        return UniqueProduct.objects.create(product=product_instance)


class Attr(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProductAttr(models.Model):
    attr = models.ForeignKey("Attr", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    value = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    attrs = models.ManyToManyField("Attr", through="ProductAttr")

    def __str__(self):
        return self.name


class UniqueProduct(models.Model):
    product = CustomForeignKey(Product, on_delete=models.PROTECT)
    attr = models.ForeignKey(ProductAttr, on_delete=models.PROTECT)
