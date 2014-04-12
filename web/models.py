# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models

import reversion

from block.models import (
    BlockModel,
    ContentModel,
)


PAGE_HOME = 'home'


class MainBlock(BlockModel):
    pass

reversion.register(MainBlock)


class Main(ContentModel):
    """Horizontal stripe - title, description, picture and URL."""

    block = models.ForeignKey(MainBlock, related_name='content')
    order = models.IntegerField()

    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='block/main/%Y/%m/%d', blank=True)
    url = models.URLField(blank=True, null=True)

    class Meta:
        # cannot put 'unique_together' on abstract base class
        # https://code.djangoproject.com/ticket/16732
        unique_together = ('block', 'moderate_state')
        verbose_name = 'Main content'
        verbose_name_plural = 'Main contents'

    def __str__(self):
        return '{} {}'.format(self.title, self.moderate_state)

    def url_publish(self):
        return reverse('web.main.publish', kwargs={'pk': self.pk})

    def url_remove(self):
        return reverse('web.main.remove', kwargs={'pk': self.pk})

    def url_update(self):
        return reverse('web.main.update', kwargs={'pk': self.pk})

reversion.register(Main)
