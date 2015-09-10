from bulbs2.utils.signals.slugs import MAX_SLUG_LENGTH
from example.app.models import FeatureType, Tag, Headline, Article
from model_mommy import mommy
import pytest


@pytest.mark.django_db
def test_set_feature_type_slug():
    ft = mommy.make(FeatureType)
    ft.save()
    assert ft.slug is not None
    assert len(ft.slug) >= MAX_SLUG_LENGTH


@pytest.mark.django_db
def test_set_tag_slug():
    tag = mommy.make(Tag)
    tag.save()
    assert tag.slug is not None
    assert len(tag.slug) >= MAX_SLUG_LENGTH


@pytest.mark.django_db
def test_set_headline_slug():
    hl = mommy.make(Headline)
    hl.save()
    assert hl.slug is not None
    assert len(hl.slug) >= MAX_SLUG_LENGTH


@pytest.mark.django_db
def test_set_article_slug():
    art = mommy.make(Article)
    art.save()
    assert art.slug is not None
    assert len(art.slug) >= MAX_SLUG_LENGTH
