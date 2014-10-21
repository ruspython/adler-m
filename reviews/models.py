from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime
from django.core.urlresolvers import reverse


class Review(models.Model):
    add_time = models.DateTimeField(_('add time'), default=datetime.now, blank=True)
    name = models.CharField(_('your name'), max_length=128)
    review = models.TextField(_('review text'))

    def __unicode__(self):
        return u'%s' % self.name

    def get_comment_link(self):
        return reverse('reviews:create_comment', args=[str(self.id)])

    def get_message(self):
        return self.review

    class Meta:
        ordering = ['-add_time']
        verbose_name = _('review')
        verbose_name_plural = _('reviews')


class Comment(models.Model):
    review = models.ForeignKey(Review, verbose_name=_('review'))
    add_time = models.DateTimeField(_('add time'), default=datetime.now, blank=True)
    author = models.ForeignKey(User, verbose_name=_('author'), blank=True, null=True)
    name = models.CharField(_('your name'), max_length=128, blank=True, null=True)
    comment = models.TextField(_('comment'), blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.comment

    def get_comment_link(self):
        return reverse('reviews:create_comment', args=[str(self.review.id)])

    def get_message(self):
        return self.comment

    class Meta:
        ordering = ['-add_time']
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
