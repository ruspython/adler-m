from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class AdlerContactApp(CMSApp):
    name = _("Contact")
    urls = ["contact.urls"]
    app_name = "contact"

apphook_pool.register(AdlerContactApp)
