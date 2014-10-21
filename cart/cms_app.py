from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class AdlerCartApp(CMSApp):
    name = _("Cart App")
    urls = ["cart.urls"]
    app_name = "cart"

apphook_pool.register(AdlerCartApp)
