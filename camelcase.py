#ask for a name
#convert name in camelcase format (firstName) to snake format (first_name):
camel_case = input("camelCase: ")
camel1 = list(camel_case)

print("snake_case: ", end="")

for letter in camel1:
    upletter = letter.isupper()

    if upletter:
        print("_", letter.lower(), sep="", end="")

    else:
        print(letter, end="")
