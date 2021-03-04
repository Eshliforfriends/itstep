def tripple_result(func):
    def wrapper_triple(*args):
        print(func(*args)*3)
    return wrapper_triple

@tripple_result
def add(a, b):
   return a + b

add(5, 5)