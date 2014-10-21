from modeltranslation.translator import translator, TranslationOptions
from .models import Blog, BlogUploadedModel


class BlogUploadedModelTranslationOptions(TranslationOptions):
    fields = ('name', 'brand', 'type', 'comment', 'note', 'series', 'manufacturer', 'color')


class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'announce', 'text')


translator.register(Blog, BlogTranslationOptions)
translator.register(BlogUploadedModel, BlogUploadedModelTranslationOptions)