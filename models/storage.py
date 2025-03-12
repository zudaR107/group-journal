# storage.py

import json
from models import Subject, JournalManager, Student


class StorageManager:
    """
    Класс для сохранения и загрузки данных журнала в JSON.
    """

    FILE_PATH = "data/journal_data.json"  # Путь к JSON-файлу

    @staticmethod
    def save_to_json(journal_manager: JournalManager) -> None:
        """Сохраняет данные JournalManager в JSON-файл."""
        data = {
            "group_name": journal_manager.group_info.group_name,
            "students": [
                {"full_name": student.full_name, "subgroup": student.subgroup}
                for student in journal_manager.group_info.students
            ],
            "subjects": [
                {"subject_name": subject.subject_name, "types": subject.types}
                for subject in journal_manager.subjects
            ]
        }

        with open(StorageManager.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @staticmethod
    def load_from_json() -> JournalManager:
        """Загружает данные из JSON-файла и создаёт объект JournalManager."""
        journal_manager = JournalManager()

        try:
            with open(StorageManager.FILE_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)

            journal_manager.set_group_name(data.get("group_name", ""))

            # Загружаем студентов
            for student_data in data.get("students", []):
                student = Student(
                    full_name=student_data["full_name"],
                    subgroup=student_data["subgroup"]
                )
                journal_manager.group_info.add_student(student)

            # Загружаем предметы
            for subject_data in data.get("subjects", []):
                subject = Subject(
                    subject_name=subject_data["subject_name"],
                    types=subject_data["types"]
                )
                journal_manager.subjects.append(subject)

        except (FileNotFoundError, json.JSONDecodeError):
            # Если файл отсутствует или повреждён, создаём пустой JournalManager
            print("Файл данных не найден или повреждён. Будет создан новый журнал.")

        return journal_manager
