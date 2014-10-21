from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class AdlerFavoriteApp(CMSApp):
    name = _("Favorite App")
    urls = ["favorite.urls"]
    app_name = "favorite"

apphook_pool.register(AdlerFavoriteApp)
