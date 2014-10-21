from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class AdlerCollectionPublicApp(CMSApp):
    name = _("Public Collection App")
    urls = ["collection_public.urls"]
    app_name = "collection_public"

apphook_pool.register(AdlerCollectionPublicApp)
