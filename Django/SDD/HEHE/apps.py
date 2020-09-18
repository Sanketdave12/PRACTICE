from django.apps import AppConfig


class HeheConfig(AppConfig):
    name = 'HEHE'
    def ready(self):
        import HEHE.signal