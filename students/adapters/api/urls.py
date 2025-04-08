from rest_framework.urls import path

from students_api.students.adapters.api.views import (
    StudentListCreateView,
    StudentRetrieveUpdateView,
)

urlpatterns = [
    path("students/", StudentListCreateView.as_view(), name="student_list"),
    path("students/<int:id>", StudentRetrieveUpdateView.as_view(), name="student_detail"),
]
