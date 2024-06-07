import pytest
from main import BooksCollector
@pytest.fixture
def collect():
    collect = BooksCollector()
    return collect
class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collect):
        collect.add_new_book('Гордость и предубеждение и зомби')
        collect.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collect.get_books_genre()) == 2

    @pytest.mark.parametrize('book_names', ['', 'Очень_большое_название_книги_которое_точно_отрицательное'])
    def test_add_new_book_add_negative_book(self, collect, book_names):
        collect.add_new_book(book_names)
        assert len(collect.get_books_genre()) == 0

    def test_set_book_genre_added_genre_book_positive_result(self, collect):
        collect.add_new_book('Летающие котята в космосе')
        collect.set_book_genre('Летающие котята в космосе', 'Фантастика')
        assert collect.books_genre.get('Летающие котята в космосе') == 'Фантастика'

    def test_set_book_genre_add_genre_is_not_list(self, collect):
        collect.add_new_book('Летающие котята в космосе')
        collect.set_book_genre('Летающие котята в космосе', 'Мяукалка')
        assert collect.books_genre.get('Летающие котята в космосе') == ''

    def test_get_book_genre_for_name_positive_result(self, collect):
        collect.add_new_book('Летающие котята в космосе')
        collect.set_book_genre('Летающие котята в космосе', 'Фантастика')
        assert collect.get_book_genre('Летающие котята в космосе') == 'Фантастика'

    def test_get_books_with_specific_genre_get_two_books_fantastic(self, collect):
        collect.books_genre = {'Летающие котята в космосе': 'Фантастика', 'Летающие котята в космосе_2': 'Фантастика', 'Летающие котята в космосе_3': 'Ужасы',
                               'Летающие котята в космосе_4': 'Мультфильмы'}
        assert len(collect.get_books_with_specific_genre('Фантастика')) == 2
    def test_get_books_genre_full_list_of_books(self, collect):
        collect.books_genre = {'Котята': 'Мультфильмы', 'Щенята': 'Детективы', 'Тараканы': 'Ужасы',
                                   'Попугаи': 'Комедии'}
        assert len(collect.get_books_genre()) == 4

    def test_get_books_for_children_two_books(self, collect):
        collect.books_genre = {'Котята': 'Мультфильмы', 'Щенята': 'Детективы', 'Тараканы': 'Ужасы',
                               'Попугаи': 'Комедии'}
        assert len(collect.get_books_for_children()) == 2

    def test_add_book_in_favorites_add_one_book(self, collect):
        collect.add_new_book('Котята')
        collect.add_book_in_favorites('Котята')
        assert len(collect.get_list_of_favorites_books()) == 1 and collect.favorites[0] == 'Котята'

    def test_add_book_in_favorites_add_two_double_book(self, collect):
        collect.add_new_book('Котята')
        collect.add_book_in_favorites('Котята')
        collect.add_book_in_favorites('Котята')
        assert len(collect.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self, collect):
        collect.add_new_book('Котята')
        collect.add_book_in_favorites('Котята')
        collect.delete_book_from_favorites('Котята')
        assert len(collect.favorites) == 0
    def test_get_list_of_favorites_books(self, collect):
        collect.add_new_book('Котята')
        collect.add_book_in_favorites('Котята')
        collect.add_new_book('Щенята')
        collect.add_book_in_favorites('Щенята')
        assert len(collect.get_list_of_favorites_books()) == 2