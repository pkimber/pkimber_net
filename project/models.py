from django.core.urlresolvers import reverse
from django.db import models

from cms.models import ContentModel


class StripeContent(ContentModel):
    """Horizontal stripe - title, description, picture and URL."""
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='cms/simple/%Y/%m/%d', blank=True)
    url = models.URLField(blank=True, null=True)

    class Meta:
        # cannot put 'unique_together' on abstract base class
        # https://code.djangoproject.com/ticket/16732
        unique_together = ('container', 'moderate_state')
        verbose_name = 'Horizontal band'
        verbose_name_plural = 'Horizontal band'

    def _get_content_set(self):
        return self.container.stripecontent_set

    def __unicode__(self):
        return unicode('{} {}'.format(self.title, self.moderate_state))
