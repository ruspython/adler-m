from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from .menu import CatalogMenu


class AdlerCatalogApp(CMSApp):
    name = _("Adler Catalog App")
    urls = ["catalog.urls"]
    app_name = "catalog"
    menus = [CatalogMenu]

apphook_pool.register(AdlerCatalogApp)