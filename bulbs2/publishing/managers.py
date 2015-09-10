from django.db import models
from django.utils import timezone


class PublishedManager(models.Manager):
    """
    provides a queryset of `PublishMixin` models whose `published` field is <= now

    >>> from datetime import datetime, timedelta
    >>> from bulbs2.content.mixins import TitleMixin, DescriptionMixin
    >>> from bulbs2.publishing.managers import PublishedManager, ScheduledManager, DraftManager
    >>> from bulbs2.publishing.mixins import PublishMixin
    >>> from django.db import models
    >>>
    >>> class Article(TitleMixin, DescriptionMixin, PublishMixin):
    ...     fun_to_read = models.BooleanField(default=True)
    ...     published_objects = PublishedManager()
    ...
    >>> article = Article.objects.create(
    ...     name="How to Write Good Django Docs",
    ...     subhead="A Masterclass",
    ...     description="Written by a total egomaniac"
    ...     fun_to_read=False)
    >>> assert article not in Article.published_objects.all()
    >>> article.published = datetime.now() - timedelta(days=1)
    >>> article.save()
    >>> assert article in Article.published_objects.all()
    """

    def get_queryset(self, *args, **kwargs):
        return super(PublishedManager, self).get_queryset(*args, **kwargs)\
            .filter(published__lte=timezone.now())\
            .exclude(published__isnull=True)


class ScheduledManager(models.Manager):
    """
    provides a queryset of `PublishMixin` models whose `published` field is > now

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
    ...
    >>> article = Article.objects.create(
    ...     name="How to Write Good Django Docs",
    ...     subhead="A Masterclass",
    ...     description="Written by a total egomaniac"
    ...     fun_to_read=False)
    >>> assert article not in Article.scheduled_objects.all()
    >>> article.published = datetime.now() + timedelta(days=1)
    >>> article.save()
    >>> assert article in Article.scheduled_objects.all()
    """

    def get_queryset(self, *args, **kwargs):
        return super(ScheduledManager, self).get_queryset(*args, **kwargs)\
            .filter(published__gt=timezone.now())\
            .exclude(published__isnull=True)


class DraftManager(models.Manager):
    """
    provides a queryset of `PublishMixin` models whose `published` field is null

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
    >>> assert article in Article.draft_objects.all()
    """

    def get_queryset(self, *args, **kwargs):
        return super(DraftManager, self).get_queryset(*args, **kwargs).filter(published__isnull=True)
