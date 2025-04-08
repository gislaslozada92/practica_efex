from students_api.students.adapters.persistence.student_model import StudentModel
from students_api.students.application.ports.student_repository import StudentRepository
from students_api.students.domain.student import Student


class StudentRepositoryImpl(StudentRepository):

    def get_all(self) -> list[Student]:
        return [self._to_domain(student) for student in StudentModel.objects.all()]

    def get_by_id(self, id: int) -> Student:
        try:
            return self._to_domain(StudentModel.objects.get(id=id))
        except StudentModel.DoesNotExist:
            return None

    def create(self, student: Student) -> Student:
        student_model = StudentModel.objects.create(
            first_name=student.first_name,
            last_name=student.last_name,
            date_of_birth=student.date_of_birth,
            grade=student.grade,
            phone=student.phone,
            email=student.email,
        )
        return self._to_domain(student_model)

    def update(self, id: int, student: Student) -> Student:
        try:
            student_model = StudentModel.objects.get(id=id)
            for key, value in student:
                setattr(student_model, key, value)
            student_model.save()
            return self._to_domain(student_model)
        except StudentModel.DoesNotExist:
            return None

    def _to_domain(self, student_model: StudentModel) -> Student:
        return Student(
            id=student_model.id,
            first_name=student_model.first_name,
            last_name=student_model.last_name,
            date_of_birth=student_model.date_of_birth,
            grade=student_model.grade,
            phone=student_model.phone,
            email=student_model.email,
        )
