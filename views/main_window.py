# main_window.py

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton,
    QLineEdit, QListWidget, QHBoxLayout, QMessageBox
)
from models.storage import StorageManager
from views.dialogs import AddEditStudentDialog, AddEditSubjectDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Электронный журнал посещаемости")
        self.setGeometry(100, 100, 800, 600)

        # Загружаем данные из JSON
        self.journal_manager = StorageManager.load_from_json()

        # Главное окно (контейнер)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)

        # Поле для ввода названия группы
        self.group_name_label = QLabel("Название группы:")
        self.group_name_edit = QLineEdit(self.journal_manager.group_info.group_name)
        self.group_name_edit.textChanged.connect(self.update_group_name)

        # Блок студентов
        layout.addWidget(self.group_name_label)
        layout.addWidget(self.group_name_edit)
        layout.addWidget(QLabel("Список студентов:"))

        self.students_list = QListWidget()
        layout.addWidget(self.students_list)
        self.update_student_list()

        # Горизонтальные кнопки для управления студентами
        student_buttons_layout = QHBoxLayout()
        self.add_student_btn = QPushButton("Добавить студента")
        self.edit_student_btn = QPushButton("Редактировать студента")
        self.delete_student_btn = QPushButton("Удалить студента")

        self.add_student_btn.clicked.connect(self.add_student)
        self.edit_student_btn.clicked.connect(self.edit_student)
        self.delete_student_btn.clicked.connect(self.delete_student)

        student_buttons_layout.addWidget(self.add_student_btn)
        student_buttons_layout.addWidget(self.edit_student_btn)
        student_buttons_layout.addWidget(self.delete_student_btn)
        layout.addLayout(student_buttons_layout)

        # Блок предметов
        layout.addWidget(QLabel("Список предметов:"))
        self.subjects_list = QListWidget()
        layout.addWidget(self.subjects_list)
        self.update_subject_list()

        # Горизонтальные кнопки для управления предметами
        subject_buttons_layout = QHBoxLayout()
        self.add_subject_btn = QPushButton("Добавить предмет")
        self.edit_subject_btn = QPushButton("Редактировать предмет")
        self.delete_subject_btn = QPushButton("Удалить предмет")

        self.add_subject_btn.clicked.connect(self.add_subject)
        self.edit_subject_btn.clicked.connect(self.edit_subject)
        self.delete_subject_btn.clicked.connect(self.delete_subject)

        subject_buttons_layout.addWidget(self.add_subject_btn)
        subject_buttons_layout.addWidget(self.edit_subject_btn)
        subject_buttons_layout.addWidget(self.delete_subject_btn)
        layout.addLayout(subject_buttons_layout)

        # Кнопка сохранения данных
        self.save_btn = QPushButton("Сохранить журнал")
        self.save_btn.clicked.connect(self.save_data)
        layout.addWidget(self.save_btn)

    def update_group_name(self):
        """Обновляет название группы при изменении текста."""
        self.journal_manager.set_group_name(self.group_name_edit.text())

    def update_student_list(self):
        """Обновляет отображение списка студентов."""
        self.students_list.clear()
        for student in self.journal_manager.group_info.students:
            self.students_list.addItem(f"{student.full_name} (Подгруппа {student.subgroup})")

    def update_subject_list(self):
        """Обновляет отображение списка предметов."""
        self.subjects_list.clear()
        for subject in self.journal_manager.subjects:
            self.subjects_list.addItem(f"{subject.subject_name} ({', '.join(subject.types)})")

    def add_student(self):
        """Открывает диалоговое окно для добавления студента."""
        dialog = AddEditStudentDialog(self)
        if dialog.exec_():
            student = dialog.get_student()
            self.journal_manager.add_student(student.full_name, student.subgroup)
            self.update_student_list()

    def edit_student(self):
        """Редактирует выбранного студента."""
        selected_index = self.students_list.currentRow()
        if selected_index == -1:
            QMessageBox.warning(self, "Ошибка", "Выберите студента для редактирования")
            return

        student = self.journal_manager.group_info.students[selected_index]
        dialog = AddEditStudentDialog(self, student)
        if dialog.exec_():
            edited_student = dialog.get_student()
            self.journal_manager.group_info.students[selected_index] = edited_student
            self.update_student_list()

    def delete_student(self):
        """Удаляет выбранного студента."""
        selected_index = self.students_list.currentRow()
        if selected_index != -1:
            self.journal_manager.remove_student_by_index(selected_index)
            self.update_student_list()

    def add_subject(self):
        """Открывает диалоговое окно для добавления предмета."""
        dialog = AddEditSubjectDialog(self)
        if dialog.exec_():
            subject = dialog.get_subject()
            self.journal_manager.add_subject(subject.subject_name, subject.types)
            self.update_subject_list()

    def edit_subject(self):
        """Редактирует выбранный предмет."""
        selected_index = self.subjects_list.currentRow()
        if selected_index == -1:
            QMessageBox.warning(self, "Ошибка", "Выберите предмет для редактирования")
            return

        subject = self.journal_manager.subjects[selected_index]
        dialog = AddEditSubjectDialog(self, subject)
        if dialog.exec_():
            edited_subject = dialog.get_subject()
            self.journal_manager.subjects[selected_index] = edited_subject
            self.update_subject_list()

    def delete_subject(self):
        """Удаляет выбранный предмет."""
        selected_index = self.subjects_list.currentRow()
        if selected_index != -1:
            self.journal_manager.remove_subject(selected_index)
            self.update_subject_list()

    def save_data(self):
        """Сохраняет данные в JSON-файл."""
        StorageManager.save_to_json(self.journal_manager)
        QMessageBox.information(self, "Сохранение", "Данные успешно сохранены!")
