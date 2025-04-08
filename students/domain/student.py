from dataclasses import dataclass
from typing import Optional
from datetime import date


@dataclass
class Student:
    id: Optional[int]
    first_name: str
    last_name: str
    date_of_birth: date
    grade: int
    phone: str
    email: str
