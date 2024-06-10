**Проект:**

  Приложение **BooksCollector**. Оно позволяет установить жанр книг, сортировать книги по возрастному ограничению, добавлять и удалять их в избранном.

**Структура:**


1. **BooksCollector** в **main.py**


2. Тесты в **tests.py**




| Метод | Описание метода | Проверка метода                                                                                |
| ------------- | ------------- |------------------------------------------------------------------------------------------------|
| add_new_book  | Добавляет новую книгу в словарь без указания жанра. Название книги может содержать максимум 40 символов. Одну и ту же книгу можно добавить только один раз  | test_add_new_book_add_two_books test_add_new_book_add_negative_book                            |
| set_book_genre  | устанавливает жанр книги, если книга есть в books_genreи её жанр входит в списокgenre | test_set_book_genre_added_genre_book_positive_result test_set_book_genre_add_genre_is_not_list |
| get_book_genre  | выводит жанр книги по её имени  | test_get_book_genre_for_name_positive_result                                                   |
| get_books_with_specific_genre  | выводит список книг с определённым жанром  | test_get_books_with_specific_genre_get_two_books_fantastic                                     |
| get_books_genre  | выводит текущий словарь books_genre  |  test_get_books_genre_full_list_of_books                                                                                              |
| get_books_for_children  | возвращает книги, которые подходят детям. У жанра книги не должно быть возрастного рейтинга  | test_get_books_for_children_two_books                                                          |
| add_book_in_favorites  | добавляет книгу в избранное. Книга должна находиться в словаре books_genre. Повторно добавить книгу в избранное нельзя | test_add_book_in_favorites_add_one_book test_add_book_in_favorites_add_two_double_book                                                       |
| delete_book_from_favorites  | удаляет книгу из избранного, если она там есть | test_delete_book_from_favorites                                                                |
| get_list_of_favorites_books  | получает список избранных книг | test_get_list_of_favorites_books                                                               |

**Запустить тесты из терминала можно такой командой:**
	
 
 	pytest -v tests.py 