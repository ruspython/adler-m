from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subscription(models.Model):
    email = models.EmailField(_('Email'))

    class Meta:
        verbose_name = _('email')
        verbose_name_plural = _('emails')