# note i just thought this was funny ...
import requests

from searchable_collection import SearchableCollection

url="https://api.tronalddump.io/search/quote?query=banks"
#lets see what he has to say about banks
data = requests.get(url).json().get("_embedded",{}).get('quotes',[])

my_list = SearchableCollection(data)

# What does he think about banks and Hillary?
print([x['value'] for x in my_list.find_all_where(tags__contains="Hillary Clinton")])
# What does he think about banks and Cruz?
print([x['value'] for x in my_list.find_all_where(tags__contains="Ted Cruz")])
# What does he think about banks and Tim?
print([x['value'] for x in my_list.find_all_where(tags__contains="Tim Kaine")])
