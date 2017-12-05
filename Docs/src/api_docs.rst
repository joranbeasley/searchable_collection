.. _api_docs:

SearchableCollection API Documentation
======================================

In General SearchableCollection attempts to mimic the functionality of a list exactly

that means you can do indexing like ``my_list[0], my_list[-1]``

and you can also do slicing like ``my_list[5:15:3]``

and you can do standard list setitems like ``my_list[6] = SomeClass()``

you can also use the normal ``x in my_list`` operator


.. seealso::

   :ref:`QUERY ARGUMENTS<query_reference>`

   :ref:`Lookups CheatSheet<comparison_modifiers>`

Available Methods
-----------------

.. _findonewhere:

.. py:classmethod:: SearchableCollection.find_one_where(**query_conditions)

   :param query_conditions: keyword pairs that describe the current search criteria
   :type query_conditions: SEE: :ref:`QUERY ARGUMENTS<query_reference>`
   :return: A single match from the collection (the *first* match found), *or None if no match is found*

    search the collection and return the first item that matches our search criteria

   .. code-block:: python

      my_collection.find_one_where(sn="123123",in_use=False)

.. _findallwhere:

.. py:classmethod:: SearchableCollection.find_all_where(**query_conditions)

   :param query_conditions: keyword pairs that describe the current search criteria
   :type query_conditions: SEE: :ref:`QUERY ARGUMENTS<query_reference>`
   :return: all of the matches from the collection
   :rtype: generator

   this will search the collection for any items matching the provided criteria

    .. code-block:: python

       for result in my_collection.find_all_where(condition1=3, condition2=4):
           do_something(result)



.. _deletewhere:

.. py:classmethod:: SearchableCollection.delete_where(**query_conditions)

   :param query_conditions: keyword pairs that describe the current search criteria
   :type query_conditions: SEE: :ref:`QUERY ARGUMENTS<query_reference>`
   :return: None

   Deletes any items in the collection that match the given search criteria

   .. code-block:: python

      my_collection.delete_where(sn__startswith="AB") # delete all things that have a sn attribute starting with "AB"

* :ref:`genindex`
* :ref:`search`