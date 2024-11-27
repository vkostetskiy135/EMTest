import json
import os
from typing import List, Dict, Optional


# Тип данных книги
Book = Dict[str, str | int]


class Library:
    """Класс для управления библиотекой книг."""

    def __init__(self, data_file: str = "library.json") -> None:
        """
        Инициализация библиотеки.

        :param data_file: Путь к файлу с данными библиотеки.
        """
        self.data_file = data_file
        self.books: List[Book] = self._load_data()

    def _load_data(self) -> List[Book]:
        """Загрузка данных из JSON-файла."""
        if os.path.exists(self.data_file):
            with open(self.data_file, "r", encoding="utf-8") as file:
                return json.load(file)
        return []

    def _save_data(self) -> None:
        """Сохранение данных в JSON-файл."""
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump(self.books, file, indent=4, ensure_ascii=False)

    def add_book(self, title: str, author: str, year: int) -> None:
        """
        Добавление новой книги в библиотеку.

        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания.
        """
        book_id = max((book["id"] for book in self.books), default=0) + 1
        new_book = {"id": book_id, "title": title, "author": author, "year": year, "status": "в наличии"}
        self.books.append(new_book)
        self._save_data()
        print(f"Книга '{title}' добавлена в библиотеку с ID {book_id}.")

    def delete_book(self, book_id: int) -> None:
        """
        Удаление книги из библиотеки.

        :param book_id: ID книги.
        """
        for book in self.books:
            if book["id"] == book_id:
                self.books.remove(book)
                self._save_data()
                print(f"Книга с ID {book_id} удалена.")
                return
        print(f"Книга с ID {book_id} не найдена.")

    def search_books(self, field: str, value: str) -> List[Book]:
        """
        Поиск книг по полю.

        :param field: Поле для поиска ('title', 'author', 'year').
        :param value: Значение для поиска.
        :return: Список найденных книг.
        """
        if field not in {"title", "author", "year"}:
            print("Некорректное поле для поиска.")
            return []

        result = [book for book in self.books if value.lower() in str(book[field]).lower()]
        return result

    def display_books(self) -> None:
        """Вывод всех книг в библиотеке."""
        if not self.books:
            print("Библиотека пуста.")
            return

        print("Список книг:")
        for book in self.books:
            print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, "
                  f"Год: {book['year']}, Статус: {book['status']}")

    def change_status(self, book_id: int, status: str) -> None:
        """
        Изменение статуса книги.

        :param book_id: ID книги.
        :param status: Новый статус ('в наличии', 'выдана').
        """
        if status not in {"в наличии", "выдана"}:
            print("Некорректный статус.")
            return

        for book in self.books:
            if book["id"] == book_id:
                book["status"] = status
                self._save_data()
                print(f"Статус книги с ID {book_id} изменён на '{status}'.")
                return
        print(f"Книга с ID {book_id} не найдена.")


def main() -> None:
    """Основная функция для запуска программы."""
    library = Library()

    while True:
        print("\nДоступные действия:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            title = input("Введите название книги: ").strip()
            author = input("Введите автора книги: ").strip()
            year = input("Введите год издания книги: ").strip()

            if year.isdigit():
                library.add_book(title, author, int(year))
            else:
                print("Год издания должен быть числом.")
        elif choice == "2":
            book_id = input("Введите ID книги для удаления: ").strip()
            if book_id.isdigit():
                library.delete_book(int(book_id))
            else:
                print("ID должен быть числом.")
        elif choice == "3":
            field = input("Введите поле для поиска (title, author, year): ").strip()
            value = input("Введите значение для поиска: ").strip()
            results = library.search_books(field, value)
            if results:
                for book in results:
                    print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, "
                          f"Год: {book['year']}, Статус: {book['status']}")
            else:
                print("Книги не найдены.")
        elif choice == "4":
            library.display_books()
        elif choice == "5":
            book_id = input("Введите ID книги для изменения статуса: ").strip()
            status = input("Введите новый статус ('в наличии', 'выдана'): ").strip()
            if book_id.isdigit():
                library.change_status(int(book_id), status)
            else:
                print("ID должен быть числом.")
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()




