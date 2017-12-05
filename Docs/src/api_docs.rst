SearchableCollection API Documentation
======================================



Available Methods
-----------------

.. py:decoratormethod:: SearchableCollection.find_one_where(**query_conditions)

   :param dict query_conditions: keyword pairs that describe the current search criteria, SEE ALSO: :ref:`QUERY ARGUMENTS`<>
   :return: A single match from the collection (the *first* match found), *or None if no match is found*

    search the collection and return the first item that matches our search criteria

   .. code-block:: python

      my_collection.find_one_where(sn="123123",in_use=False)


.. py:decoratormethod:: SearchableCollection.find_one_where(**query_conditions)

   :param dict query_conditions: keyword pairs that describe the current search criteria, SEE ALSO: :ref:`QUERY ARGUMENTS`<>
   :return: all of the matches from the collection
   :rtype: generator

   this will search the collection for any items matching the provided criteria

    .. code-block:: python

       for result in my_collection.find_all_where(condition1=3, condition2=4):
           do_something(result)



.. py:decoratormethod:: SearchableCollection.delete_where(**query_conditions)

   :param dict query_conditions: keyword pairs that describe the current search criteria, SEE ALSO: :ref:`QUERY ARGUMENTS`<>
   :return: None

   Deletes any items in the collection that match the given search criteria

   .. code-block:: python

      my_collection.delete_where(sn__startswith="AB") # delete all things that have a sn attribute starting with "AB"