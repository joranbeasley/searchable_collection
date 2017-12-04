import re
from operator import lt, contains, gt, ge, le, eq


def startswith(x, y):
    return x.startswith(y)


def endswith(x, y):
    return x.endswith(y)


def is_in(x, y):
    """
    effectively operator.in

    :param x: needle
    :param y: haystack
    :return: x in y
    """
    return x in y


def re_match(x, y, flags=0):
    """
    effectively operator.re_match

    :param x: search_text
    :param y: pattern
    :param flags: re.I|re.DOTALL|... see re documentation
    :return: re.match(pattern,search_text,flags)
    """
    return re.match(y, x, flags)


def re_search(x, y, flags=0):
    """
    effectively operator.re_search

    :param x: search_text
    :param y: pattern
    :param flags: re.I|re.DOTALL|... see re documentation
    :return: re.search(pattern,search_text,flags)
    """
    return re.search(y, x, flags)


class SimpleComparator:
    comparator_dict = {
        # numeric (mostly)
        'lt': lt, 'gt': gt, "lte": le, 'gte': ge, 'ge': ge, 'le': le, 'eq': eq,
        # string matching
        'contains': contains, "in": is_in, 'startswith': startswith, "endswith": endswith,
        # regular expressions
        "match": re_match, "search": re_search,
        # helper to not shadow in if its the only part of the argument .find_where(in=[1,2,3]) =>.find_where(is_in=[1,2,3])
        'is_in': is_in
    }

    def __init__(self, item, comparator, negate=False):
        self.item = item
        self.comparator = comparator
        self.comparator_fn = self.comparator_dict[comparator]
        self.negate = negate

    def __eq__(self, other):
        try:
            if self.negate:
                return not self.comparator_fn(self.item, other)
            return self.comparator_fn(self.item, other)
        except (ValueError, TypeError, AttributeError):
            return self.negate

