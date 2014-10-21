from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class AdlerSubscriptionsApp(CMSApp):
    name = _("Adler Subscription App")
    urls = ["subscription.urls"]
    app_name = "subscription"

apphook_pool.register(AdlerSubscriptionsApp)