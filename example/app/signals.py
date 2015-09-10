from bulbs2.utils.signals.slugs import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import FeatureType, Tag, Headline, Article


@receiver(pre_save, sender=FeatureType)
def set_feature_type_slug(sender, instance, **kwargs):
    if instance.name:
        instance.slug = slugify(instance.name)


@receiver(pre_save, sender=Tag)
def set_tag_slug(sender, instance, **kwargs):
    if instance.name:
        instance.slug = slugify(instance.name)


@receiver(pre_save, sender=Headline)
def set_headline_slug(sender, instance, **kwargs):
    if instance.title:
        instance.slug = slugify(instance.title)


@receiver(pre_save, sender=Article)
def set_article_slug(sender, instance, **kwargs):
    if instance.title:
        instance.slug = slugify(instance.title)
