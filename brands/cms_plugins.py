from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from .models import Brand, BrandsPluginConfig


class BrandsPlugin(CMSPluginBase):
    module = _("Adler-M")
    name = _("Brands Plugin")
    render_template = "brands/brands_plugin.html"
    model = BrandsPluginConfig

    def render(self, context, instance, placeholder):
        context.update({'brands': Brand.objects.all()})
        context.update({'instance': instance})
        return context


plugin_pool.register_plugin(BrandsPlugin)