.. _query_reference:

Query Reference
===============

Field lookups are how you specify the meat of a query.
They’re specified as keyword arguments to the following SearchableCollection methods


.. seealso::

   Method :py:meth:`find_all_where(**query_conditions)<SearchableCollection.find_all_where>`
      Documentation of the :py:meth:`SearchableCollection.find_all_where` method

   Method :py:meth:`find_one_where(**query_conditions)<SearchableCollection.find_one_where>`
      Documentation of the :py:meth:`SearchableCollection.find_one_where` method

   Method :py:meth:`delete_where(**query_conditions)<SearchableCollection.delete_where>`
      Documentation of the :py:meth:`SearchableCollection.delete_where` method

Basic lookups \*\*conditions arguments take the form **<field>__<lookuptype>=value**. (That’s a double-underscore).


For example:

>>> entry_objects.filter(pub_date__lte=datetime.now())

would find all the *things* in entry_objects where :py:data:`entry_object.pub_date <= now()`\*

\*\*if :py:data:`entry_object` is a dict it would find all entries where :py:data:`entry_object['pub_date'] <= now()`

additionally you can **negate** any of the lookuptypes by prepending :py:data:`not_<lookuptype>`

>>> entry_objects.filter(pub_date__not_lte=datetime.now())

would find all entry_objects where :py:data:`entry_object.pub_date` **IS NOT** less than or equal to :py:meth:`now()`

 * *you **do not** have to supply both the field and the lookuptype*
 * *if you ommit the* **lookuptype***, it will default to* :py:data:`eq`
 * *if you ommit the* **field**, *it will default to the root level object*
 * *if you ommit either, you do not need the double underscore(* :py:data:`__` *)*

.. seealso:: :ref:`Lookups CheatSheet<comparison_modifiers>`


Query LookupType Reference
--------------------------

.. py:data:: eq

   tests a field for equality, this is the default lookuptype if None is specified

    >>> entry_objects.find_all_where(serial_number__eq="SN123123")
    >>> entry_objects.find_all_where(serial_number="SN123123")

    are both equivelent statements, however when using the negated form you *must* specify :py:data:`eq`

    >>> entry_objects.find_all_where(serial_number__not_eq="SN123123")

    is the negated form.

String LookupTypes
__________________




.. py:data:: contains

   tests a field to see if it contains a value (or substring)

   >>> author_objects.find_all_where(articles_id_list__contains=15)

   would return all the :py:data:`author_objects`, that had field named :py:attr:`articles_id_list`, that contained the article_id of 15

   >>> author_objects.find_all_where(articles_id_list__not_contains=15)

   would return all the :py:data:`author_objects`, that had field named :py:attr:`articles_id_list`, that DID NOT contain the article_id of 15

.. py:data:: in

   tests a field for membership in a set.

   >>> entry_objects.find_all_where(status__in=["PENDING","ACTIVE"])
   >>> entry_objects.find_all_where(status__not_in=["CANCELLED","FAILED"])

   **note**: *if you ommit the* **field** *you must access this as* :py:data:`is_in`

   >>> entry_objects.find_all_where(is_in=[1,3,7,9])

.. py:data:: startswith

   tests a field for startswith

   >>> entry_objects.find_all_where(serial_number__startswith("SN76"))

   finds all the objects with a :py:attr:`serial_number` attribute that starts with :py:data:`"SN79"`

   >>> entry_objects.find_all_where(serial_number__not_startswith("SN76"))

   finds all the objects that **DO NOT** have a :py:attr:`serial_number` attribute that starts with :py:data:`"SN79"`


.. py:data:: endswith

   tests a field for endswith

   >>> entry_objects.find_all_where(serial_number__endswith("3"))

   finds all the objects with a :py:attr:`serial_number` attribute that ends with :py:data:`"3"`

   >>> entry_objects.find_all_where(serial_number__not_endswith("3"))

   finds all the objects that **DO NOT** have a :py:attr:`serial_number` attribute that ends with :py:data:`"3"`


.. py:data:: search

   tests a field for re.search, that is searches can appear anywhere in the target

   >>> entry_objects.find_all_where(serial_number__search("3[0-9]"))

   finds all the objects with a :py:attr:`serial_number` attribute that contains 3 followed by any digit

   >>> entry_objects.find_all_where(serial_number__not_search("3[0-9]"))

   finds all the objects that **DO NOT** have a :py:attr:`serial_number` attribute that contains 3 followed by any digit


.. py:data:: match

   tests a field for re.match, that is matches only match from the beginning

   >>> entry_objects.find_all_where(serial_number__match("3[0-9]"))

   finds all the objects with a :py:attr:`serial_number` attribute that starts with a 3 followed by any digit

   >>> entry_objects.find_all_where(serial_number__not_match("3[0-9]"))

   finds all the objects that **DO NOT** have a :py:attr:`serial_number` attribute that starts with a 3 followed by any digit


General LookupTypes
___________________

.. py:data:: lt

   less than

   >>> entry_objects.find_all_where(cost__lt(3.50)) # x < 3.50
   >>> entry_objects.find_all_where(cost__not_lt(3.50)) # x >= 3.50


.. py:data:: lte

   less than or equal

   >>> entry_objects.find_all_where(cost__lte(3.50)) # x <= 3.50
   >>> entry_objects.find_all_where(cost__not_lte(3.50)) # x > 3.50


.. py:data:: gt

   greater than

   >>> entry_objects.find_all_where(rating__gt(9)) # x > 9
   >>> entry_objects.find_all_where(rating__not_gt(9)) # x <= 9

.. py:data:: gte

   greater than or equal

   >>> entry_objects.find_all_where(rating__gte(9)) # x >= 9
   >>> entry_objects.find_all_where(cost__not_gte(9)) # x < 9


Lookups Than Span Sub-Objects
-----------------------------

SearchableCollections offer a powerful and intuitive way to “follow” relationships in lookups,
taking care of the search for you automatically, behind the scenes.
To span a sub-object, just use the field name of sub-objects, separated by double underscores,
until you get to the field you want.

>>> entry_objects.filter(blog__name='Beatles Blog')

this assumes you have an object with a field named "blog", blog has a field named "name"

>>> entry = {"blog":{"name":...,"date":...,"author":{"name":...,"publications":[...]}}

this will locate the entry that has a blog, with a name field of "Beatles Blog"

This spanning can be as deep as you like

>>> entry_objects.filter(blog__author__name='Lennon')






* :ref:`genindex`
* :ref:`search`