from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class AdlerBrandsApp(CMSApp):
    name = _("Brands App")
    urls = ["brands.urls"]
    app_name = "brands"

apphook_pool.register(AdlerBrandsApp)