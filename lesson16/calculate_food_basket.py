def calculate_food_basket(food_basket: dict, exchange_rate:float) -> float:
    value = 0
    for item in food_basket:
        value += food_basket[item] * exchange_rate
    return value

the_basket = {
    'bread': 1.2,
    'milk': 1.6,
    'potato': 0.4,
    'sunflower oil': 2,
    'meat': 2.4
}

print(calculate_food_basket(the_basket, 27.5))