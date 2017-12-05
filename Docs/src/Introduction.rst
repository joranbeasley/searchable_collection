examples using python primatives
================================

Creating A SearchableList
-------------------------

you can create a list just like a normal list (well mostly)

.. code-block:: python
    :linenos:

    from searchable_collection import SearchableCollection
    some_other_list = [1,2,3,4,5,6]
    my_list = SearchableCollection(some_other_list)
    print(list(my_list.find_all_where(in=[4,5])))

or you can simply append items as needed 

.. code-block:: python
    :linenos:

    from searchable_collection import SearchableCollection
    some_other_list = [1,2,3,4,5,6]
    my_list = SearchableCollection()
    for i in some_other_list:
        my_list.append(i)        
    print(list(my_list.find_all_where(in=[2,6])))

or you can use extend

    from searchable_collection import SearchableCollection
    some_other_list = [1,2,3,4,5,6]
    my_list = SearchableCollection()
    my_list.extend(some_other_list)
    print(list(my_list.find_all_where(in=[2,6])))

What can go in a Searchable Collection?
---------------------------------------

well pretty much anything... and it should just work, originally it was designed specifically with classes in mind, however it should really work just fine with anything

 .. code-block:: python
    :linenos:

    original_data = [[1,2,3],[3,4,5,'e'],{"w":7},"pie","apple",{"e":67},1,2,3,4,5,6]
    my_list = SearchableCollection(original_data)
    
    print(list(my_list.find_all_where(e=67))
    print(list(my_list.find_all_where(contains="e"))
    print(list(my_list.find_all_where(contains=2))
    print(list(my_list.find_all_where(contains=3))
    
    # do an re.match (only matches "pie")
    print(list(my_list.find_all_where(match="p.e"))
    # do an re.search (matches both "pie" and "apple")
    print(list(my_list.find_all_where(search="p.e"))
    
it starts getting even more interesting with nested dictionaries

.. code-block:: python
    :linenos:

    my_list = SearchableCollection()
    my_list.append({"sub_dict":{"anumber":56,"aword":"apple","alist":[1,2,3]})
    my_list.append({"sub_dict":{"anumber":26,"aword":"pineapple","alist":[7,8,9]})
    my_list.append({"sub_dict":{"anumber":126,"aword":"orange","alist":[7,18,19]})

    # d['sub_dict']['anumber'] == 26
    print(list(my_list.find_all_where(sub_dict__anumber=26))
    
    # d['sub_dict']['anumber'] > 50
    print(list(my_list.find_all_where(sub_dict__anumber_gt=50))
    
    # d['sub_dict']['aword'] == "orange"
    print(list(my_list.find_all_where(sub_dict__aword="orange"))
    
    # "n" in d['sub_dict']['aword']
    print(list(my_list.find_all_where(sub_dict__aword__contains="n"))
    
    # d['sub_dict']['aword'].endswith("le")
    print(list(my_list.find_all_where(sub_dict__aword__endswith="le"))
    
    # 3 in d['sub_dict']['alist']
    print(list(my_list.find_all_where(sub_dict__alist__contains=3))


.. seealso::

   :ref:`query_reference`

   :ref:`api_docs`



What Modifiers Can I Use
------------------------
the complete list of modifiers is as follows

.. _comparison_modifiers:

.. code-block:: text

    __contains   -  x in y    
    __in         -  y in x # note that if the field is ommited it is replaced with is_in `...where(is_in=...)`
    __startswith -  x.startswith(y)
    __endswith   -  x.endswith(y)
    __search     -  re.search(y,x)
    __match      -  re.match(y,x)
    # numeric operators
    __gt         -  x > y
    __gte        -  x >= y
    __lt         -  x < y
    __lte        -  x <= y
    __eq         -  x == y # in general this is the assumed operation and can be ommited

    
you can optionally negate any of the operators

.. code-block:: text

    __not_contains   -  x not in y    
    __not_in         -  y not in x      
    __not_startswith -  not x.startswith(y)
    __not_endswith   -  not x.endswith(y)
    __not_search     -  not re.search(y,x)
    __not_match      -  not_re.match(y,x)
    # numeric operators
    __not_gt         -  not x > y  # or x <= y
    __not_gte        -  not x >= y # or x < y
    __not_lt         -  not x < y  # or x >= y
    __not_lte        -  x <= y     # or x > y
    __not_eq         -  x != y



* :ref:`genindex`
* :ref:`search`

