number = int(input('Voer een getal in: '))

result = 0
output = ''
for i in range(1, number + 1):
    result += i

    '''
        line if else statement
        this  one line is the same as:
        if i != number:
            output += str(i) + ' + '
        else:
            output += str(i) + ' ='
    '''
    output += str(i) + ' + ' if i != number else str(i) + ' ='

print(output, result)
