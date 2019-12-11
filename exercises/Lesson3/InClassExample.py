def create_grid(n):
    output = ""
    for x in range(n):
        for y in range(n):
            output += '*'
        output += '\n'
    print(output)


user_input = int(input('voer een getal in: '))
create_grid(user_input)
