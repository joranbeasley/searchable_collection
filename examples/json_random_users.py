import requests

from searchable_collection import SearchableCollection

n_users=50
users_data = []
print("Creating Users:")
for i in range(n_users):
    print("%d/%d"%(i,n_users))
    users_data.append(requests.get("https://randomuser.me/api").json()['results'][0])

users_list = SearchableCollection(users_data)

print(len(list(users_list.find_all_where(name__last__startswith="ro"))),"Users whose last names start with 'ro'")
print(len(list(users_list.find_all_where(name__last__startswith="j"))),"Users whose first names start with 'j'")


