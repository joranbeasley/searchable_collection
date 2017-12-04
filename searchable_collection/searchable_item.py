from operator import eq
from searchable_collection import SimpleComparator

class SearchableItem:
    collection = None
    _item_index = -1

    def __init__(self, target_ob, collection):
        self.collection = collection
        self.target = target_ob
        self.original_delete = getattr(target_ob, "delete", lambda *a: 1)

        try:
            self.target.collection = self.collection
            self.target.delete = lambda *a: SearchableItem.delete(self)
            self.target.item_index = self._item_index
        except:
            pass

    def set_item_index(self, val):
        self._item_index = val
        try:
            self.target.item_index = val
        except:
            pass

    def delete(self):
        self.collection.delete(self)

    def __eq__(self, other):
        return eq(self.target, other)

    def __getattr__(self, item):
        if hasattr(self.target, item):
            return getattr(self.target, item)
        elif isinstance(self.target,dict) and item in self.target:
            return self.target[item]
        elif item == "to_dict":
            return lambda: getattr(self.target, '__dict__', self.target)
        elif item in SimpleComparator.comparator_dict:
            return SimpleComparator(self.target, item)
        elif item.startswith("not_") and item[4:] in SimpleComparator.comparator_dict:
            return SimpleComparator(self.target, item[4:],negate=True)
        try:
            rest, end_part = item.split("__", 1)
        except:
            # print("CANNOT SPLIT ITEM %r???" % item)
            print("No Attribute %r on %r" % (item,self.target))
            return None


        target = result = self
        while hasattr(result, rest) or isinstance(result,dict) and rest in result:
            target = result
            if isinstance(target,dict):
                result = target[rest]
            else:
                result = getattr(target, rest)
            try:
                rest, end_part = end_part.split("__", 1)
            except:
                break

        if end_part in SimpleComparator.comparator_dict:
            return SimpleComparator(result, end_part)
        elif end_part.startswith("not_") and end_part[4:] in SimpleComparator.comparator_dict:
            return SimpleComparator(result, end_part[4:], negate=True)
        return getattr(result, end_part, result)