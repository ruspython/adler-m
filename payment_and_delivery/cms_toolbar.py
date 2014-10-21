from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar


@toolbar_pool.register
class H2BToolbar(CMSToolbar):

    def populate(self):
        if self.is_current_app:
            menu = self.toolbar.get_or_create_menu('how2buy', _('Delivery methods'))
            menu.add_sideframe_item(_('Countries'), url=reverse('admin:payment_and_delivery_country_changelist'))
            menu.add_sideframe_item(_('Cities'), url=reverse('admin:payment_and_delivery_city_changelist'))