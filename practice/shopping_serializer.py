import pickle

shopping_list = [ {
    'bread': 1.2,
    'milk': 1.6,
    'potato': 0.4,
    'sunflower oil': 2} ,
    {'meat': 2.4,
    'eggs': 0.4,
    'fish': 2.4
}]

#pickle
with open('shopping_list.pkl', 'wb') as f:
    data_s = pickle.dump(shopping_list, f)
    print(data_s)

with open('shopping_list.pkl', 'rb') as f:
    data_new = pickle.load(f)
    print(data_new)

import json

#jsonh
with open('shopping_list.json', 'w') as n:
    json.dump(shopping_list, n)

with open('shopping_list.json', 'rb') as n:
    data_new_j = json.load(n)
    print(data_new_j)



