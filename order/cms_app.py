from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class AdlerOrdersApp(CMSApp):
    name = _("Adler Orders App")
    urls = ["order.urls"]
    app_name = "order"

apphook_pool.register(AdlerOrdersApp)