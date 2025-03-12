from typing import List

class Subject:
    """
    Класс, представляющий предмет.
    subject_name: название предмета (например, "Математика")
    types: список типов занятий (Лекция, Семинар, Лабораторная работа)
    """

    def __init__(self, subject_name: str, types: List[str] = None):
        self.subject_name = subject_name
        self.types = types if types else []  # По умолчанию пустой список

    def add_type(self, lesson_type: str) -> None:
        """Добавляет тип занятия (если он ещё не добавлен)."""
        if lesson_type not in self.types:
            self.types.append(lesson_type)

    def remove_type(self, lesson_type: str) -> None:
        """Удаляет тип занятия (если он существует)."""
        if lesson_type in self.types:
            self.types.remove(lesson_type)

    def __repr__(self):
        return f"Subject(subject_name={self.subject_name!r}, types={self.types})"
