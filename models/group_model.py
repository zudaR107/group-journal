from typing import List

class Student:
    """
    Класс, описывающий студента.
    full_name: строка с ФИО в формате «Иванов И. И.»
    subgroup: номер подгруппы (может быть int или str, в зависимости от ваших нужд)
    """

    def __init__(self, full_name: str, subgroup: int = 0):
        self.full_name = full_name
        self.subgroup = subgroup

    def __repr__(self):
        return f"Student(full_name={self.full_name!r}, subgroup={self.subgroup!r})"


class GroupInfo:
    """
    Класс, описывающий всю информацию о группе:
    group_name: название группы (например, «ИС-21»)
    students: список экземпляров Student
    """

    def __init__(self, group_name: str = ""):
        self.group_name = group_name
        self.students: List[Student] = []

    def add_student(self, student: Student) -> None:
        """Добавляет студента в конец списка."""
        self.students.append(student)

    def remove_student_by_index(self, index: int) -> None:
        """
        Удаляет студента по индексу из списка.
        Не забудьте проверять, что index в допустимых пределах.
        """
        if 0 <= index < len(self.students):
            self.students.pop(index)

    def remove_student(self, student: Student) -> None:
        """Удаляет конкретный объект Student из списка (если он там есть)."""
        if student in self.students:
            self.students.remove(student)

    def __repr__(self):
        return f"GroupInfo(group_name={self.group_name!r}, students={self.students})"
