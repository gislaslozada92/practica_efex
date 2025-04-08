from students_api.students.application.ports.student_repository import StudentRepository
from students_api.students.domain.student import Student


class StudentService:

    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def create_student(self, data: dict):
        student = Student(
            first_name=data["first_name"],
            last_name=data["last_name"],
            date_of_birth=data["date_of_birth"],
            grade=data["grade"],
            phone=data["phone"],
            email=data["email"],
        )
        return self.repository.create(student)

    def get_all_students(self) -> list[Student]:
        return self.repository.get_all()

    def get_student_by_id(self, id: int) -> Student | None:
        return self.repository.get_by_id(id)

    def update_student(self, id: int, data: dict) -> Student | None:
        student = Student(
            first_name=data["first_name"],
            last_name=data["last_name"],
            date_of_birth=data["date_of_birth"],
            grade=data["grade"],
            phone=data["phone"],
            email=data["email"],
        )
        return self.repository.update(id, student)
