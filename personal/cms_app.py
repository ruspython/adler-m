from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class AdlerPersonalApp(CMSApp):
    name = _("Personal data App")
    urls = ["personal.urls"]
    app_name = "personal"

apphook_pool.register(AdlerPersonalApp)
