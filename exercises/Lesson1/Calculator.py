number1 = int(input('Voer een getal in: '))
op = input('Voer een operator in (+, -, *, /): ')
number2 = int(input('Voer een getal in: '))

output = 0

if op == '+':
    output = number1 + number2
elif op == '-':
    output = number1 - number2
elif op == '*':
    output = number1 * number2
elif op == '/':
    output = number1 / number2
else:
    output = 'Not a valid operator'

print(number1, op, number2, '=', output)
