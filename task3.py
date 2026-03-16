class Book:
    def __init__(self, name, autor, count=1):
        self.name = name
        self.autor = autor
        self.count = count

    def __str__(self):
        return f"'{self.name}' автор: {self.autor}, кількість: {self.count}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, new_book):
        for book in self.books:
            if book.name == new_book.name and book.autor == new_book.autor:
                book.count += 1  # додаємо +1 до наявної кількості
                print(f"Кількість книги '{book.name}' оновлено. Тепер у наявності {book.count}.")
                return
        self.books.append(new_book)
        print(f"Додано нову книгу '{new_book.name}' автор: {new_book.autor}.")

    def user_take_book(self, name, autor):
        for book in self.books:
            if book.name == name and book.autor == autor:
                if book.count > 0:
                    book.count -= 1
                    print(f"Ви взяли книгу '{book.name}'. Залишилось {book.count}.")
                    return
                else:
                    print(f"Книга '{book.name}' є, але її зараз немає у наявності.")
                    return
        print(f"Книга '{name}' автор: {autor} не знайдена в бібліотеці.")

    def show_books(self):
        if not self.books:
            print("Бібліотека порожня.")
        else:
            print("Список книг у бібліотеці:")
            for book in self.books:
                print(book)


library = Library()

library.add_book(Book("Гаррі Поттер", "Дж. К. Роулінг"))
library.add_book(Book("Гаррі Поттер", "Дж. К. Роулінг"))  # збільшуємо кількість +1
library.add_book(Book("Гаррі Поттер", "Інший Автор"))     # інший автор — окрема книга
library.add_book(Book("Війна і мир", "Лев Толстой"))

library.show_books()

library.user_take_book("Гаррі Поттер", "Дж. К. Роулінг")
library.user_take_book("Війна і мир", "Лев Толстой")
library.user_take_book("Неіснуюча книга", "Автор")

library.show_books()