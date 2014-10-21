from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class AdlerCollectionApp(CMSApp):
    name = _("Collection App")
    urls = ["collection.urls"]
    app_name = "collection"

apphook_pool.register(AdlerCollectionApp)
