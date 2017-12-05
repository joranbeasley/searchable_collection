import random

from test_searchablecollection_data import SimpleSearchExampleClass
from searchable_collection import SearchableCollection


def test_create_searchlist():
    search_list = SearchableCollection()
    for i in range(50):
        search_list.append(SimpleSearchExampleClass.generate())

    assert len(search_list) == 50
    assert search_list[0].string_field1.startswith("a st")
    return search_list


def test_get_slice():
    search_list = test_create_searchlist()
    assert search_list[2:5] == [search_list[2], search_list[3], search_list[4]]


def test_searchlist_extend():
    search_list = test_create_searchlist()
    next_3 = [SimpleSearchExampleClass.generate() for _ in range(3)]
    search_list.extend(next_3)
    assert search_list[-1] is next_3[-1]


def test_searchlist_pop():
    search_list = test_create_searchlist()
    assert search_list[-1] is search_list.pop(-1)


def test_searchlist_pynative():
    collection = SearchableCollection()
    collection.append(5)
    assert collection[0] == 5
    collection.append([1, 2, 3])
    assert collection[-1] == [1, 2, 3]


def test_searchlist_delete():
    search_list = test_create_searchlist()
    item = random.choice(search_list)
    assert item in search_list
    search_list.delete(item)
    assert item not in search_list
    item2 = random.choice(search_list)
    assert item2 in search_list
    item2.delete()
    assert item2 not in search_list
    item3 = search_list[0]
    assert item3 in search_list
    search_list.delete(0)
    assert item3 not in search_list


def test_searchlist_delete_where():
    search_list = test_create_searchlist()
    item = random.choice(search_list)
    assert item in search_list
    search_list.delete_where(string_field2=item.string_field2)
    assert item not in search_list
    assert not any(x.string_field2 == item.string_field2 for x in search_list)


def test_to_dict():
    search_list = SearchableCollection()
    search_list.append(5)
    search_list.append([1, 2, 3])
    search_list.append(SimpleSearchExampleClass.create("asd", "dsa", 1, 2, 3, [1, 2], ['a', 'b'],
                                                       SimpleSearchExampleClass.generate(False)))
    search_list[-1].subclass.x={"asd":{"status":"ok"}}
    assert search_list.find_one_where(subclass__x__asd__status="ok") == search_list[-1]
    assert 5 in search_list.to_dicts()

def test_setitem():
    search_list = test_create_searchlist()
    d = {'a':532,'b':"Hello"}
    search_list[3] = d
    assert d is search_list[3]
    assert search_list.find_one_where(a=532,b="Hello") is d
def test_searchlist_insert():
    search_list = test_create_searchlist()
    new_ssec = SimpleSearchExampleClass.generate()
    search_list.insert(0, new_ssec)
    assert search_list[0] is new_ssec


def test_searchlist_indexing():
    search_list = test_create_searchlist()
    for i, val in enumerate(search_list):
        assert val is search_list[i]


def test_searchlist_simplesearch():
    my_list = test_create_searchlist()
    my_list.append("apple pie")
    assert my_list[3] is my_list.find_one_where(int_field1=my_list[3].int_field1)
    assert my_list.find_one_where(int_field1=5000000) is None
