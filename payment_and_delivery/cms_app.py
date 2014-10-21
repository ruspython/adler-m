from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class PaymentAndDeliveryApp(CMSApp):
    name = _("Payment and delivery")
    urls = ["payment_and_delivery.urls"]
    app_name = "payment_and_delivery"

apphook_pool.register(PaymentAndDeliveryApp)
