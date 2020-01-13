array = ['array', 'of', 'strings']


def add(x):
    res = x + '!'
    return res


mapped_items = list(map(add, array))
mapped_items_lambda = list(map(lambda x: x + '!', array))
print(mapped_items)
print(mapped_items_lambda)
