from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class AdlerPartnersApp(CMSApp):
    name = _("Adler Partners App")
    urls = ["partners.urls"]
    app_name = "partners"

apphook_pool.register(AdlerPartnersApp)