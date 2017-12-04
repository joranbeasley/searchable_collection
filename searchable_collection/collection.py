from searchable_collection.item import SearchableItem





class SearchableCollection:
    def __init__(self,list_initial=[], master=None):
        self.master = master
        self.items = []
        self.extend(list_initial)

    def __getitem__(self, index):
        """
        allows us to index into our OrderList just like a normal array

        :param index: the integer index of the Order to access
        :return: the order at the specified index
        """
        if isinstance(index,slice):
            return [i.target for i in self.items[index]]
        return self.items[index].target

    def __iter__(self):
        """
        allow orders to be iterated over
        :return: an iterator of all the orders
        """
        return (item.target for item in self.items[:])

    def __len__(self):
        return len(self.items)

    def _reindex(self):
        """
        reassigns indexes to all orders in self.orders, this should not be called directly in general

        :return:
        """
        for i, item in enumerate(self.items):
            item.set_item_index(i)

    def extend(self, other_list):
        for item in other_list:
            self.append_item(item, False)
        self._reindex()

    def pop(self, index=-1):
        item = self.items.pop(index)
        return item.target

    def insert(self, index, item, reindex=True):
        return self.insert_item(index, item, reindex)

    def append(self, item, reindex=True):
        return self.append_item(item, reindex)

    def insert_item(self, index, item, reindex=True):
        self.items.insert(index, SearchableItem(item, self))
        if reindex:
            self._reindex()
        return self.items[-1].target

    def append_item(self, item, reindex=True):
        self.items.append(SearchableItem(item, self))
        if reindex:
            self._reindex()
        return self.items[-1].target

    def delete(self, item):
        """
        delete a given order
        :param item: an integer index or an order instance
        :return:
        """
        if isinstance(item, int) and item not in self.items:
            del self.items[item]
        else:
            self.items.remove(item)
        self._reindex()

    def find_one_where(self, **kwargs):
        """

        order = orders.find_one_where(sn="123123")
        order = orders.find_one_where(sn="123123",reading_type="Fat")

        :param kwargs:Accepts same params as Order constructor (sn devType reading_type, etc)
        :return: the first matching order found or None
        """
        try:
            return next(self.find_all_where(**kwargs))
        except StopIteration:
            return None

    def find_all_where(self, **kwargs):
        """
        orders = list(orders.find_all_where(sn="123123"))
        for item in orders.find_all_where(sn="123123",reading_type="Fat"): ...

        :params : Accepts same params as Order constructor (sn devType reading_type, etc)
        :return: an iterator of all orders matching the provided criteria
        """
        def test_value(item,key,value):
            result = getattr(item, key, None)
            if callable(result):
                try:
                    result = result()
                except TypeError:
                    try:
                        return result(value)
                    except Exception as e:
                        return False
            return result == value
        for item in self.items[:]:
            if all(test_value(item,key,val) for key, val in kwargs.items()):
                yield item.target

    def delete_where(self, **kwargs):
        '''

        orders.delete_where(sn="123123")
        orders.delete_where(sn="123123",reading_type="Fat")

        :params : Accepts same params as Order constructor (sn devType reading_type, etc)
        :return: None
        '''
        self.items = [item for item in self.items if item not in list(self.find_all_where(**kwargs))]
        self._reindex()

    def to_dicts(self):
        '''
        convert to a list of dictionaries and return it
        :return: a list of dictionaries
        '''
        return [item.to_dict() for item in self.items]



