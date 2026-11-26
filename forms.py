"""Customer form validation using Django's forms framework, standalone (no Django project)."""
import os

import django
from django.conf import settings

if not settings.configured:
    settings.configure(
        USE_I18N=False,
        USE_TZ=True,
        SECRET_KEY=os.environ.get("DJANGO_SECRET_KEY", "dev-only-insecure-key"),
        INSTALLED_APPS=["django.contrib.auth", "django.contrib.contenttypes"],
    )
    django.setup()

from django import forms  # noqa: E402
from django.core.validators import RegexValidator  # noqa: E402


class CustomerForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(
        max_length=20,
        validators=[RegexValidator(r"^\+?[\d\s\-()]{7,20}$", "Enter a valid phone number.")],
    )
    address = forms.CharField(max_length=255)
    contact = forms.CharField(max_length=100)


def flatten_errors(form):
    """Return a list of 'Field: message' strings for flashing."""
    return [f"{field.capitalize()}: {msg}" for field, msgs in form.errors.items() for msg in msgs]
