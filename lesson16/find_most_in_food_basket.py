def find_most_in_food_basket(food_basket: dict, max_cost = True) -> set:
    basket_items = list(food_basket.values())

    if max_cost == True:
        max_basket = max(basket_items)
        max_set = []
        for item in food_basket:
            if food_basket.get(item) == max_basket:
                max_set.append(item)
        return set(max_set)
    else:
        min_basket = min(basket_items)
        min_set = []
        for item in food_basket:
            if food_basket.get(item) == min_basket:
                min_set.append(item)
        return set(min_set)

the_basket = {
    'bread': 1.2,
    'milk': 1.6,
    'potato': 0.4,
    'sunflower oil': 2,
    'meat': 2.4,
    'eggs': 0.4,
    'fish': 2.4
}

print(find_most_in_food_basket(the_basket))
print(find_most_in_food_basket(the_basket,max_cost = False))