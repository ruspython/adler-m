from django.db import models
from django.utils.translation import ugettext_lazy as _
from djangocms_text_ckeditor.fields import HTMLField


class Faq(models.Model):
    name = models.CharField(_('your name'), max_length=128)
    question = models.TextField(_('faq question'))
    answer = HTMLField(_('faq answer'), blank=True)
    ordering = models.IntegerField(_('ordering'), default=10)

    def __unicode__(self):
        return u'%s' % self.question

    class Meta:
        ordering = ['ordering']
        verbose_name = _('faq')
        verbose_name_plural = _('faqs')
