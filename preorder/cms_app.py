from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class AdlerPreOrderApp(CMSApp):
    name = _("PreOrder App")
    urls = ["preorder.urls"]
    app_name = "preorder"

apphook_pool.register(AdlerPreOrderApp)
