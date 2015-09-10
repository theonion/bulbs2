from datetime import timedelta

from django.utils import timezone
from example.app.models import Headline
from model_mommy import mommy
import pytest


@pytest.mark.django_db
def test_draft():
    hl = mommy.make(Headline, published=None)
    hl.save()
    assert hl in Headline.draft_objects.all()
    assert hl not in Headline.scheduled_objects.all()
    assert hl not in Headline.published_objects.all()


@pytest.mark.django_db
def test_scheduled():
    future = timezone.now() + timedelta(days=1)
    hl = mommy.make(Headline, published=future)
    hl.save()
    assert hl not in Headline.draft_objects.all()
    assert hl in Headline.scheduled_objects.all()
    assert hl not in Headline.published_objects.all()


@pytest.mark.django_db
def test_published():
    past = timezone.now() - timedelta(days=1)
    hl = mommy.make(Headline, published=past)
    hl.save()
    assert hl not in Headline.draft_objects.all()
    assert hl not in Headline.scheduled_objects.all()
    assert hl in Headline.published_objects.all()
