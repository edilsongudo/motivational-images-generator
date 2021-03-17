from django.apps import AppConfig


class PasswordsmanagerConfig(AppConfig):
    name = 'passwordsmanager'

    def ready(self):
        import passwordsmanager.signals
