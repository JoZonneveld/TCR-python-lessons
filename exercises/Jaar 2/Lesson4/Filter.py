def is_even(x):
    return x % 2 == 0


array = [3, 2, 3, 4]

print(list(filter(is_even, array)))
