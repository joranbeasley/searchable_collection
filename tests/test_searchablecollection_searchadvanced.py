import random

import pytest
from test_searchablecollection_data import SimpleSearchExampleClass
from searchable_collection.searchable_collection import SearchableCollection


def test_create_searchlist():
    search_list = SearchableCollection()
    for i in range(50):
        search_list.append(SimpleSearchExampleClass.generate())

    assert len(search_list) == 50
    assert search_list[0].string_field1.startswith("a st")
    return search_list


def test_search_natives():
    search_list = SearchableCollection()
    search_list.extend(
        [[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9], [9, 10, 11, 'e'], 9, 10, "pie", "turkey", "apple", {'a': 5},
         {'e': 7}])
    assert search_list.find_one_where(is_in=[10, 4]) == 10
    assert search_list.find_one_where(is_in=[10, 9]) == 9
    assert search_list.find_one_where(e=7) == {'e':7}
    assert sorted(search_list.find_all_where(is_in=[10, 9])) == [9, 10]

    assert list(search_list.find_all_where(contains=2)) == [[1, 2, 3]]
    assert list(search_list.find_all_where(contains=3)) == [[1, 2, 3], [3, 4, 5]]

    assert list(search_list.find_all_where(contains='e')) == [[9, 10, 11, 'e'], 'pie', 'turkey', 'apple', {'e': 7}]
    assert list(search_list.find_all_where(startswith='p')) == ["pie"]
    assert list(search_list.find_all_where(endswith='e')) == ["pie", "apple"]
    assert list(search_list.find_all_where(match='p.e')) == ["pie"]
    assert list(search_list.find_all_where(search='p.e')) == ["pie", "apple"]

    assert list(search_list.find_all_where(not_contains=3)) == [[5, 6, 7], [7, 8, 9], [9, 10, 11, 'e'], 9, 10, "pie",
                                                                "turkey", "apple", {'a': 5}, {'e': 7}]


def test_searchclasses():
    search_list = test_create_searchlist()

    assert all(x.int_field1 > 3000 for x in search_list.find_all_where(int_field1__gt=3000))
    assert all(x.int_field1 <= 3000 for x in search_list.find_all_where(int_field1__not_gt=3000))
    assert all(x.subclass.int_field1 > 5000 for x in search_list.find_all_where(subclass__int_field1__gt=5000))
    assert all(
        x.subclass.string_field2 == "Rabits" for x in search_list.find_all_where(subclass__string_field1="Rabits"))


def test_exception_cases():
    search_list = test_create_searchlist()
    search_list[0].test22 = lambda z, b, c: [z, b, c]
    search_list.find_one_where(test22="gasd")
