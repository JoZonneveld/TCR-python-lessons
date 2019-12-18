user_input = ''
age = 0

# Change `your name` to your own name
while user_input != 'your name' or age != 23:
    user_input = input('Voer uw naam in: ')
    age = int(input('Voer uw leeftijd in: '))

    # Change `your name` to your own name
    if user_input == 'your name':
        print('this is my name')
    else:
        print('this is not my name')

    if age == 23:
        print('that is my age')
    else:
        print('that is not my age')
