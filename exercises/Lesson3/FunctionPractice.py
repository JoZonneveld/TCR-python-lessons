import math


def power_off(x):
    for i in range(1, x + 1):
        print(str(i) + '² =', math.pow(i, 2))


def power_off_total(x):
    result = 0
    for i in range(1, x + 1):
        result += math.pow(i, 2)
    return result


user_input = int(input('Vul een getal in: '))

power_off(user_input)
print(power_off_total(user_input))
