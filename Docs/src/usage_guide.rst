SearchableCollection Usage Guide
================================

Simple Access
-------------

you may access a Searchablelist exactly the same as a normal list for the most part

.. code-block:: python
    :linenos:

    from searchable_collection import SearchableCollection
    some_other_list = [1,2,3,4,5,6]
    my_list = SearchableCollection(some_other_list)
    print(my_list[2],my_list[-1])  # 3 and 6
    print(len(my_list),my_list.pop(3),len(my_list))
    my_list.append(5)
    print(len(my_list),my_list[-1])

Adding Element To Searchable List
---------------------------------

you should be able to add elements to a Searchable list the same as if it were a normal list



.. code-block:: python
    :linenos:

    from searchable_collection import SearchableCollection

    my_list = SearchableCollection()
    my_list.append(4)
    my_list.extend(["a",66,{'asd':'dsa','b':5}])

Searching For Elements
----------------------

this is really the whole purpose of this module, to provide a flexible ORM like interface to searching though lists
I doubt its super efficient, so i wouldnt recommend using it with huge lists, but it should be able to search
a few hundred records near instantly

Single Nested Element Search
____________________________

When searching we can use all of our :ref:`Comparison Search Modifiers <comparison_modifiers>`.



.. code-block:: python
    :linenos:

    from searchable_collection import SearchableCollection
    raw_data = [1,2,3,"pie","apple",[1,2,"e",3],[3,4,5],{"x":7}]
    my_list = SearchableCollection(raw_data)

    # lets find all the items that have an e
    items_with_e = my_list.find_all_where(contains=e)

    # lets find all the items that are in [1,"pie",[3,4,5]]
    items_in_list = my_list.find_all_where(is_in=[1,"pie",[3,4,5])

    # lets find all the items that startwith "a"
    items_startwith_e = my_list.find_all_where(startswith="a"))

    # we can also negate ANY of our modifiers
    # lets find all the items that DO NOT startwith "a"
    items_startwith_e = my_list.find_all_where(not_startswith="a"))

    # lets find all the items that endwith "e"
    items_endwith_e = my_list.find_all_where(endswith="e"))

    # lets find all the items that are less than 3
    items_lessthan = my_list.find_all_where(lt=3))


Single Nested Attribute Search
______________________________

Like Single Nested Element Search we can still use all our :ref:`Comparison Search Modifiers <comparison_modifiers>`. but this time we will be accessing the attributes of a class

the format that we need to use for this is

.. code-block:: python

    find_all_where(<attribute_name>__<modifier> = <value>)
    #the modifier is of coarse optional
    find_all_where(<attribute_name> = <value>)
    #or the modifier can be negated
    find_all_where(<attribute_name>__not_<modifier> = <value>)




.. code-block:: python
    :linenos:

    from searchable_collection import SearchableCollection
    raw_data = [{"x":i,"y":j} for i,j in zip(range(25),range(100,74,-1))]
    my_list = SearchableCollection(raw_data)

    # lets find all the items that have x == 5
    items_with_x5 = my_list.find_all_where(x=5)

    # lets find all the items that have x <= 5
    items_lte_5 = my_list.find_all_where(x__lte=5)

    # lets find all the items that have x <= 5 && y > 97
    items_lte_5 = my_list.find_all_where(x__lte=5,y__gt=97)

    # lets find all the items that have x <= 5 && y != 97
    items_lte_5 = my_list.find_all_where(x__lte=5,y__not_eq=97)

Multi Level Nested Attribute Search
___________________________________

now imagine we had some objects like the following, and of coarse you can still use all the :ref:`Comparison Search Modifiers <comparison_modifiers>`

.. code-block:: python

   class TestClass():
        def __init__(self,a,b,c,d):
            self.a=a
            self.b_list = {"b":b,"c":{"val":c,"next":d}}
        def __repr__(self):
            return str(self)
        def __str__(self):
            return "<TC="+str([self.a,[self.b_list['b'],[self.b_list['c']['val'],self.b_list['c']['next']]])+">"

   objects = SearchableCollection([ TestClass(*range(4)),
                TestClass(*range(1,5)),
                TestClass(*range(3,8)),
                TestClass(*range(6,11))
              ])
   print(objects[0])

now we can actually dive in and access sub-attibutes of our class

.. code-block:: python

   objects.find_all_where(contains="a") # zero level search (just a modifier)

   objects.find_all_where(a=3) # single level search
   objects.find_all_where(a__in=[3,6]) # single level search with modifier

   objects.find_all_where(a=3) # single level search
   objects.find_all_where(a__in=[3,6]) # single level search with modifier

   objects.find_all_where(b_list__b=3) # 2nd level search
   objects.find_all_where(b_list__b__not_in=[3,5]) # 2nd level search with negated modifier

   objects.find_all_where(b_list__c__val=4) # 3rd level search
   objects.find_all_where(b_list__c__val__gt=7) # 3rd level search with negated modifier

you can continue indefinately ... although i imagine the deeper you have to
go the slower it will be, but it should be fine for smallish lists


* :ref:`genindex`
* :ref:`search`

