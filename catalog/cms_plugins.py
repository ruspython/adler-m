from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from .models import ItemType, Item


class ModelTypesPlugin(CMSPluginBase):
    module = _("Adler-M")
    name = _("Model types Plugin")
    render_template = "catalog/model_types_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'types': ItemType.objects.all()})
        context.update({'instance': instance})
        return context


class CatalogIndexPlugin(CMSPluginBase):
    module = _("Adler-M")
    name = _("Catalog index Plugin")
    render_template = "catalog/index_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({
            'new': Item.objects.filter(status_new=True)[:9],
            'soon': Item.objects.filter(status_on_the_way=True)[:9],
            'sale': Item.objects.filter(status_sale=True)[:9],
        })
        context.update({'instance': instance})
        return context


plugin_pool.register_plugin(ModelTypesPlugin)
plugin_pool.register_plugin(CatalogIndexPlugin)