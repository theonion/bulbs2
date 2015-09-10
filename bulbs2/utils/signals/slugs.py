from django.conf import settings
from django.template.defaultfilters import slugify as _slugify


MAX_SLUG_LENGTH = getattr(settings, "MAX_SLUG_LENGTH", 50)


def slugify(value, length=MAX_SLUG_LENGTH):
    """runs the given value through django's slugify filter and slices it to a given length

    :param value: the value you want turned into a slug
    :type value: str

    :param length: the maximum length of the slug
    :type length: int

    :return: the slugified version of the input value sliced to the length value
    :rtype: str
    """
    slug = _slugify(value)[:length]
    while slug.endswith("-"):
        slug = slug[:-1]
    return slug
