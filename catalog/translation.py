from modeltranslation.translator import translator, TranslationOptions
from .models import Item


class ItemTranslationOptions(TranslationOptions):
    fields = ('name', 'brand', 'type', 'comment', 'note', 'series', 'manufacturer', 'color')


class AccessoryTranslationOptions(TranslationOptions):
    fields = ('name', 'note', 'series', 'manufacturer', 'color')


class BookTranslationOptions(TranslationOptions):
    fields = ('name', 'author', 'note')


translator.register(Item, ItemTranslationOptions)