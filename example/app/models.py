from bulbs2.content.mixins import TitleMixin, DescriptionMixin, BodyMixin
from bulbs2.content.models import Bulbs2BaseFeatureType
from bulbs2.publishing.managers import PublishedManager, ScheduledManager, DraftManager
from bulbs2.publishing.mixins import PublishMixin
from bulbs2.tagging.models import Bulbs2BaseTag
from django.db import models


class FeatureType(Bulbs2BaseFeatureType):
    pass


class Tag(Bulbs2BaseTag):
    pass


class BaseContent(PublishMixin, TitleMixin, DescriptionMixin):
    class Meta(object):
        abstract = True

    feature_type = models.ForeignKey(FeatureType)
    tags = models.ManyToManyField(Tag)


class Headline(BaseContent):
    published_objects = PublishedManager()
    scheduled_objects = ScheduledManager()
    draft_objects = DraftManager()


class Article(BaseContent, BodyMixin):
    published_objects = PublishedManager()
    scheduled_objects = ScheduledManager()
    draft_objects = DraftManager()
