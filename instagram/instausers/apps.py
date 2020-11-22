from django.apps import AppConfig


class InstausersConfig(AppConfig):
    name = 'instausers'

    def ready(self):
        import instausers.signals
