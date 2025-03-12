# dialogs.py

from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox, QCheckBox
)
from models.group_model import Student
from models.subject_model import Subject

class AddEditStudentDialog(QDialog):
    """
    Диалоговое окно для добавления/редактирования студента.
    """

    def __init__(self, parent=None, student: Student = None):
        super().__init__(parent)
        self.setWindowTitle("Добавить / Редактировать студента")
        self.setModal(True)

        layout = QVBoxLayout(self)

        self.name_label = QLabel("Фамилия И. О.:")
        self.name_edit = QLineEdit()

        self.subgroup_label = QLabel("Номер подгруппы:")
        self.subgroup_edit = QSpinBox()
        self.subgroup_edit.setRange(1, 10)

        if student:
            self.name_edit.setText(student.full_name)
            self.subgroup_edit.setValue(student.subgroup)

        self.ok_btn = QPushButton("ОК")
        self.ok_btn.clicked.connect(self.accept)

        layout.addWidget(self.name_label)
        layout.addWidget(self.name_edit)
        layout.addWidget(self.subgroup_label)
        layout.addWidget(self.subgroup_edit)
        layout.addWidget(self.ok_btn)

    def get_student(self) -> Student:
        """Возвращает объект Student с введёнными данными."""
        return Student(
            full_name=self.name_edit.text(),
            subgroup=self.subgroup_edit.value()
        )


class AddEditSubjectDialog(QDialog):
    """
    Диалоговое окно для добавления/редактирования предмета.
    """

    def __init__(self, parent=None, subject: Subject = None):
        super().__init__(parent)
        self.setWindowTitle("Добавить / Редактировать предмет")
        self.setModal(True)

        layout = QVBoxLayout(self)

        self.name_label = QLabel("Название предмета:")
        self.name_edit = QLineEdit()

        self.lecture_check = QCheckBox("Лекция")
        self.seminar_check = QCheckBox("Семинар")
        self.lab_check = QCheckBox("Лабораторная работа")

        if subject:
            self.name_edit.setText(subject.subject_name)
            if "Лекция" in subject.types:
                self.lecture_check.setChecked(True)
            if "Семинар" in subject.types:
                self.seminar_check.setChecked(True)
            if "Лабораторная работа" in subject.types:
                self.lab_check.setChecked(True)

        self.ok_btn = QPushButton("ОК")
        self.ok_btn.clicked.connect(self.accept)

        layout.addWidget(self.name_label)
        layout.addWidget(self.name_edit)
        layout.addWidget(self.lecture_check)
        layout.addWidget(self.seminar_check)
        layout.addWidget(self.lab_check)
        layout.addWidget(self.ok_btn)

    def get_subject(self) -> Subject:
        """Возвращает объект Subject с введёнными данными."""
        types = []
        if self.lecture_check.isChecked():
            types.append("Лекция")
        if self.seminar_check.isChecked():
            types.append("Семинар")
        if self.lab_check.isChecked():
            types.append("Лабораторная работа")

        return Subject(
            subject_name=self.name_edit.text(),
            types=types
        )
