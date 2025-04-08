from abc import ABC, abstractmethod

from students_api.students.domain.student import Student


class StudentRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[Student]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Student:
        pass

    @abstractmethod
    def create(self, student: Student) -> Student:
        pass

    @abstractmethod
    def update(self, id: int, student: Student) -> Student:
        pass
