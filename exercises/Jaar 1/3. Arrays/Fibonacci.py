number = int(input('Voer een getal in: '))

result = []

for i in range(number):
    if i == 0:
        result.append(0)
    elif i == 1 or i == 2:
        result.append(1)
    else:
        result.append(result[i - 2] + result[i - 1])
print(result)
