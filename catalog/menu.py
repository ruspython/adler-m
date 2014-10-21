from menus.base import NavigationNode
from cms.menu_bases import CMSAttachMenu
from menus.menu_pool import menu_pool
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


class CatalogMenu(CMSAttachMenu):
    name = _('catalog menu')

    def get_nodes(self, request):
        return [
            NavigationNode(_('All catalog'), reverse('catalog:item-list'), 'catalog'),
            NavigationNode(_('Novelties'), reverse('catalog:novelties'), 'novelties'),
            NavigationNode(_('Pre-order'), reverse('catalog:pre-order'), 'pre-order'),
            NavigationNode(_('Promo and sales'), reverse('catalog:sale'), 'sale'),
            NavigationNode(_('Back in stock'), reverse('catalog:back-in-stock'), 'back-in-stock'),
            NavigationNode(_('Accessories'), reverse('catalog:accessories'), 'accessories'),
            NavigationNode(_('Literature'), reverse('catalog:books'), 'literature'),
        ]


menu_pool.register_menu(CatalogMenu)