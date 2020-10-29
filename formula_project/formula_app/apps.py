from django.apps import AppConfig


class FormulaAppConfig(AppConfig):
    name = 'formula_app'
    def ready(self):
        import formula_app.signals

