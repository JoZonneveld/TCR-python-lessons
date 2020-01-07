array = ['Hello', 'Not', 'Yes']


def add_exclamation_mark(x):
    res = x + "!"
    return res


print(list(map(add_exclamation_mark, array)))
