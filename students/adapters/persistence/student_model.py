from django.db import models


class StudentModel(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    grade = models.IntegerField()
    phone = models.CharField()
    email = models.CharField()

    class Meta:
        app_label = "students_persistence"
