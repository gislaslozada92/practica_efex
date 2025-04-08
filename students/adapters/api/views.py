from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from students_api.students.adapters.api.serializer import (
    StudentInputSerializer,
    StudentOutputSerializer,
)
from students_api.students.adapters.persistence.student_repository_impl import (
    StudentRepositoryImpl,
)
from students_api.students.application.use_cases.student_service import StudentService


repository = StudentRepositoryImpl()
service = StudentService(repository)


class StudentListCreateView(APIView):
    def get(self, request):
        students = service.get_all_students()
        data = [StudentOutputSerializer(s).data for s in students]
        return Response(data, status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentInputSerializer(data=request.data)
        if serializer.is_valid():
            student = service.create_student(serializer.validated_data)
            return Response(student, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class StudentRetrieveUpdateView(APIView):
    def get(self, id, request):
        student = service.get_student_by_id(id)
        if student:
            return Response(student, status.HTTP_200_OK)
        return Response({"datail": "Not found."}, status.HTTP_404_NOT_FOUND)

    def patch(self, id, request):
        student = service.get_student_by_id(id)
        if not student:
            return Response({"datail": "Not found."}, status.HTTP_404_NOT_FOUND)

        serializer = StudentInputSerializer(data=request.data)
        if serializer.is_valid():
            student = service.update_student(id, serializer.validated_data)
            return Response(student, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
