from django.db import models


class Bulbs2BaseFeatureType(models.Model):
    """
    provides a base implementation for a loose hierarchy of content

    >>> from bulbs2.content.models import Bulbs2BaseFeatureType
    >>>
    >>> class FeatureType(Bulbs2BaseFeatureType):
    ...     pass
    ...
    >>> ft = FeatureType.objects.create(name="News in Brief")
    """

    class Meta(object):
        abstract = True

    name = models.CharField(max_length=512, unique=True)
    slug = models.SlugField(max_length=512, unique=True, blank=True)
