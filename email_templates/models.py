from django.db import models
from django.utils.translation import ugettext_lazy as _


class EmailTemplate(models.Model):
    name = models.CharField(_('name'), max_length=128)
    slug = models.SlugField(_('code'), max_length=128, unique=True,
                            help_text=_('for use in program code. Example:'
                                        'send_templated_email(\'template_code\', request.POST)'))
    recipients = models.CharField(_('recipients'), max_length=512,
                                  help_text=_('email or comma separated list of emails'))
    sender = models.CharField(_('sender'), max_length=256, null=True, blank=True)
    subject = models.CharField(_('subject'), max_length=256)
    template = models.TextField(_('email body template'), help_text=_('Django template tags and filters are available'))
    description = models.TextField(_('template description'), blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = _('email template')
        verbose_name_plural = _('email templates')