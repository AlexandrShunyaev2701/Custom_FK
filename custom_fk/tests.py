from django.test import TestCase
from .models import Product, Attr, ProductAttr, UniqueProduct


class CustomFKTestCase(TestCase):
    '''Тест моделей с использованием кастомного FK'''
    def setUp(self) -> None:
        # Создаем несколько объектов Attr
        self.attr1 = Attr.objects.create(name='Attr1')
        self.attr2 = Attr.objects.create(name='Attr2')

        # Создаем объект Product
        self.product = Product.objects.create(name='Product1')

        # Создаем объект ProductAttr, связывающий Product с Attr
        self.product_attr1 = ProductAttr.objects.create(product=self.product,
                                                        attr=self.attr1,
                                                        value='Value1')
        self.product_attr2 = ProductAttr.objects.create(product=self.product,
                                                        attr=self.attr2,
                                                        value='Value2')

    def test_custom_fk(self):
        # Создаем объект UniqueProduct с помощью нашего кастомного FK
        unique_product = UniqueProduct.objects.create(product=self.product,
                                                      attr=self.product_attr1)

        # Проверяем, что объект UniqueProduct был создан успешно
        self.assertIsNotNone(unique_product)

    def test_custom_related_manager(self):
        # Получаем объект Product
        product = Product.objects.get(name='Product1')

        # Получаем связанный объексты через кастомный внешний ключ
        unique_product = product.uniqueproduct_set.all()

        # Проверяем, что обратное связывание через кастомный внешний ключ 
        # работает корректно
        self.assertIsNotNone(unique_product)
