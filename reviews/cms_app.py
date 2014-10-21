from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class AdlerReviewsApp(CMSApp):
    name = _("Adler Reviews App")
    urls = ["reviews.urls"]
    app_name = "reviews"

apphook_pool.register(AdlerReviewsApp)