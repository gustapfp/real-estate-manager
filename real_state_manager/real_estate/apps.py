import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RealEstateConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"  # pyright: ignore[reportAssignmentType]
    name = "real_state_manager.real_estate"
    verbose_name = _("Real Estate")

    def ready(self):
        with contextlib.suppress(ImportError):
            import real_state_manager.real_estate.signals  # noqa: F401, PLC0415  # pyright: ignore[reportMissingImports]
