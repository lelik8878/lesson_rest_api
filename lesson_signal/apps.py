from django.apps import AppConfig


class LessonSignalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lesson_signal'

    def ready(self):
        import lesson_signal.signals
