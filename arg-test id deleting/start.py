with open("args.txt", "r") as file:
    contents = file.readlines()

with open("args.txt", "w") as file:
    file.write('')

with open("args.txt", "a") as file:
    for str in contents:
        if str.find('ID') == -1:
            file.write(str)
        else:
            print(str)