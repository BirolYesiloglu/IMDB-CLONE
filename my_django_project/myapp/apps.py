# myapp/apps.py
from django.apps import AppConfig

class MyappConfig(AppConfig):
    name = 'myapp'
    label = 'myapp_label'

    def ready(self):
        import myapp.signals