from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class SubscriptionFormPlugin(CMSPluginBase):
    module = _("Adler-M")
    name = _("Subscription form Plugin")
    render_template = "subscription/form_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


plugin_pool.register_plugin(SubscriptionFormPlugin)