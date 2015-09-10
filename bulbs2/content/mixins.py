from django.db import models


class TitleMixin(models.Model):
    """
    provides fields `title`, `subhead`, `slug`

    >>> from bulbs2.content.mixins import TitleMixin
    >>> from django.db import models
    >>>
    >>> class Article(TitleMixin):
    ...     fun_to_read = models.BooleanField(default=True)
    ...
    >>> article = Article.objects.create(
    ...     name="How to Write Good Django Docs",
    ...     subhead="A Masterclass",
    ...     fun_to_read=False)
    """

    class Meta(object):
        abstract = True

    title = models.CharField(max_length=512, unique=True)
    slug = models.SlugField(max_length=512, unique=True, blank=True)
    subhead = models.CharField(max_length=512)

    def __str__(self):
        return self.title


class DescriptionMixin(models.Model):
    """
    provides a `description` field

    >>> from bulbs2.content.mixins import TitleMixin, DescriptionMixin
    >>> from django.db import models
    >>>
    >>> class Article(TitleMixin, DescriptionMixin):
    ...     fun_to_read = models.BooleanField(default=True)
    ...
    >>> article = Article.objects.create(
    ...     name="How to Write Good Django Docs",
    ...     subhead="A Masterclass",
    ...     description="Written by a total egomaniac",
    ...     fun_to_read=False)
    """

    class Meta(object):
        abstract = True

    description = models.TextField(null=True, default=None, blank=True)


class BodyMixin(models.Model):
    """
    provides a `body` text field

    >>> from bulbs2.content.mixins import TitleMixin, DescriptionMixin, BodyMixin
    >>> from django.db import models
    >>>
    >>> class Article(TitleMixin, DescriptionMixin):
    ...     fun_to_read = models.BooleanField(default=True)
    ...
    >>> article = Article.objects.create(
    ...     name="How to Write Good Django Docs",
    ...     subhead="A Masterclass",
    ...     description="Written by a total egomaniac",
    ...     body="Blah blah blah blah blah",
    ...     fun_to_read=False)
    """

    class Meta(object):
        abstract = True

    body = models.TextField(null=True, default=None, blank=True)
