from django.utils.translation import ugettext_lazy as _


CMS_PLACEHOLDER_CONF = {
    'logo': {
        'name': _('Logo'),
        'plugins': ['PicturePlugin',],
    },
    'cart_about_discounts': {
        'name': _('About discounts'),
        'plugins': ['TextPlugin', 'PicturePlugin', 'LinkPlugin'],
    },
}