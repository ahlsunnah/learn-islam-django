from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "learn_islam.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import learn_islam.users.signals  # noqa F401
        except ImportError:
            pass
