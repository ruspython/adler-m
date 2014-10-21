from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from .models import Blog


class BlogPlugin(CMSPluginBase):
    module = _("Adler-M")
    name = _("Blog Plugin")
    render_template = "blog/blog_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'articles': Blog.objects.all()[:2]})
        context.update({'instance': instance})
        return context


plugin_pool.register_plugin(BlogPlugin)

