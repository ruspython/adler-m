from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar


@toolbar_pool.register
class CatalogToolbar(CMSToolbar):

    def populate(self):
        if self.is_current_app:
            menu = self.toolbar.get_or_create_menu('catalog', _('Catalog'))
            menu.add_sideframe_item(_('Edit items'), url=reverse('admin:catalog_item_changelist'))
            menu.add_sideframe_item(_('XML import from file'), url=reverse('admin:xml_import'))
            menu.add_sideframe_item(_('1C import'), url=reverse('admin:soap_import'))