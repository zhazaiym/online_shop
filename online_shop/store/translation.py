from .models import Product, Category, SubCategory, Review
from modeltranslation.translator import TranslationOptions,register


@register(Category)
class ProductTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(SubCategory)
class ProductTranslationOptions(TranslationOptions):
    fields = ('subcategory_name',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
        fields = ('product_name', 'description')

@register(Review)
class ProductTranslationOptions(TranslationOptions):
      fields = ('comment',)