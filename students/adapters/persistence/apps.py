from django.apps import AppConfig


class StudentsPersistenceConfig(AppConfig):
    default_auto_field = "students.adapters.persistence"
    name = "students_persistence"
