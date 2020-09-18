from django.apps import AppConfig


class MamaraConfig(AppConfig):
    name = 'MAMARA'
    def ready(self):
        import MAMARA.signal
