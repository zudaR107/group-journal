from typing import List
from models import GroupInfo, Student, Subject


class JournalManager:
    """
    Главный класс для управления журналом.
    Содержит:
    - group_info: информация о группе (GroupInfo)
    - subjects: список предметов (List[Subject])
    """

    def __init__(self):
        self.group_info = GroupInfo()  # Информация о группе
        self.subjects: List[Subject] = []  # Список предметов

    def set_group_name(self, name: str) -> None:
        """Задаёт название группы."""
        self.group_info.group_name = name

    def add_student(self, full_name: str, subgroup: int) -> None:
        """Добавляет студента в список."""
        student = Student(full_name, subgroup)
        self.group_info.add_student(student)

    def remove_student_by_index(self, index: int) -> None:
        """Удаляет студента по индексу."""
        self.group_info.remove_student_by_index(index)

    def add_subject(self, subject_name: str, types: List[str]) -> None:
        """Добавляет предмет с указанными типами занятий."""
        subject = Subject(subject_name, types)
        self.subjects.append(subject)

    def remove_subject(self, index: int) -> None:
        """Удаляет предмет по индексу."""
        if 0 <= index < len(self.subjects):
            self.subjects.pop(index)

    def __repr__(self):
        return f"JournalManager(group_info={self.group_info}, subjects={self.subjects})"