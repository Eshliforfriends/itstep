import pickle
#pickle

with open('shopping_list.pkl', 'rb') as f:
    data_new = pickle.load(f)
    print(data_new)

import json
#jsonh
with open('shopping_list.json', 'rb') as n:
    data_new_j = json.load(n)
    print(data_new_j)



