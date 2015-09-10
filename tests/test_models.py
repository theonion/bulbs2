from example.app.models import FeatureType, Tag, Headline, Article
from model_mommy import mommy
import pytest


@pytest.mark.django_db
def test_feature_type_model_fields():
    ft = mommy.make(FeatureType)
    for field in ("name", "slug"):
        assert hasattr(ft, field)


@pytest.mark.django_db
def test_tag_model_fields():
    tag = mommy.make(Tag)
    for field in ("name", "slug"):
        assert hasattr(tag, field)


@pytest.mark.django_db
def test_headline_model_fields():
    hl = mommy.make(Headline)
    for field in ("title", "slug", "subhead", "description", "feature_type", "tags"):
        assert hasattr(hl, field)


@pytest.mark.django_db
def test_article_model_fields():
    art = mommy.make(Article)
    for field in ("title", "slug", "subhead", "description", "body", "feature_type", "tags"):
        assert hasattr(art, field)
