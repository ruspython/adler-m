from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from .models import Banner


class SuperbannerPlugin(CMSPluginBase):
    module = _("Adler-M")
    name = _("Superbanner Plugin")
    render_template = "superbanner/superbanner_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'banners': Banner.objects.all()})
        context.update({'instance': instance})
        return context


plugin_pool.register_plugin(SuperbannerPlugin)