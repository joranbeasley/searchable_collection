import random

from searchable_collection import SearchableCollection

def create_random_dict():
    return {
        "status":random.choice("ok warn error".split()),
        "int_value1":random.randint(1,10),
        "int_value10":random.randint(10,100),
        "int_value100":random.randint(100,1000),
        "float_value":random.random(),
    }

my_list = SearchableCollection()
n_entries = 50
my_list.extend([create_random_dict() for _ in range(n_entries)])


# #Get all the dictionaries with status = "ok"
# print(list(my_list.find_all_where(status="ok")))
#
# #Get all the dictionaries with status != "ok"
# print(list(my_list.find_all_where(status__not_eq="ok")))
#
# #Get all the dictionaries where (d['int_value1'] > 5 && d['int_value10'] <= 50)
# print(list(my_list.find_all_where(int_value1__gt=5,int_value10__lte=50)))
#
# #Get all the dictionaries where (d['int_value1'] in [5,3,8] && d['int_value10'] <= 50)
# print(list(my_list.find_all_where(int_value1__in=[5,3,8],int_value10__lte=50)))
#
# #Get all the dictionaries where (d['int_value1'] not in [5,8] && d['int_value10'] <= 25 && d['int_value_100'] > 700)
# print(list(my_list.find_all_where(int_value1__not_in=[3,8],int_value10__lte=25,int_value100__gt=700)))
#

# we can attach sub dictionaries and search those as well
for d in my_list:
    d['extra'] = create_random_dict()

print(list(my_list.find_all_where(extra__int_value1__in=[5,6])))
