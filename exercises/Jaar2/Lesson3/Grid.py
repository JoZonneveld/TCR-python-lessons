def create_grid(n):
    for x in range(n):
        output = ""
        for y in range(n):
            output += '*'
        print(output)


user_input = int(input("vul een getal in: "))
create_grid(user_input)
