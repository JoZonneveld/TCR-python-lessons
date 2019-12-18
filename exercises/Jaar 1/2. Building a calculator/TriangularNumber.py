number = int(input('Voer een getal in: '))

result = 0
output = ''
for i in range(1, number + 1):
    result += i
    if i != number:
        output += str(i) + ' + '
    else:
        output += str(i) + ' ='

print(output, result)
