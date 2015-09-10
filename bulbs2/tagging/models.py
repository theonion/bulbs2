from django.db import models


class Bulbs2BaseTag(models.Model):
    """
    provides a base implementation for tagging

    >>> from bulbs2.tagging.models import Bulbs2BaseTag
    >>>
    >>> class Tag(Bulbs2BaseTag):
    ...     pass
    ...
    >>> tag = Tag(name="So Hot Right Now!")
    """

    class Meta(object):
        abstract = True

    name = models.CharField(max_length=512, unique=True)
    slug = models.SlugField(max_length=512, unique=True, blank=True)
