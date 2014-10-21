from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class AdlerFaqApp(CMSApp):
    name = _("Adler Faq App")
    urls = ["faq.urls"]
    app_name = "faq"

apphook_pool.register(AdlerFaqApp)
