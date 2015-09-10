from django.db import models


class PublishMixin(models.Model):
    """
    provides a nullable `published` field and an auto-tracked `modified` field

    >>> from datetime import datetime, timedelta
    >>> from bulbs2.content.mixins import TitleMixin, DescriptionMixin
    >>> from bulbs2.publishing.managers import PublishedManager, ScheduledManager, DraftManager
    >>> from bulbs2.publishing.mixins import PublishMixin
    >>> from django.db import models
    >>>
    >>> class Article(TitleMixin, DescriptionMixin, PublishMixin):
    ...     fun_to_read = models.BooleanField(default=True)
    ...     published_objects = PublishedManager()
    ...     scheduled_objects = ScheduledManager()
    ...     draft_objects = DraftManager()
    ...
    >>> article = Article.objects.create(
    ...     name="How to Write Good Django Docs",
    ...     subhead="A Masterclass",
    ...     description="Written by a total egomaniac"
    ...     fun_to_read=False)
    >>> assert article not in Article.published_objects.all()
    >>> assert article in Article.draft_objects.all()
    >>> article.published = datetime.now() + timedelta(days=1)
    >>> article.save()
    >>> assert article in Article.scheduled_objects.all()
    """

    class Meta(object):
        abstract = True

    published = models.DateTimeField(null=True, default=None, blank=True)
    modified = models.DateTimeField(auto_now=True)
