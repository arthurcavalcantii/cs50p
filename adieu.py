import inflect
p = inflect.engine()

mylist = []

while True:
        try:
            user_input = input("Name: ")
            mylist.append(user_input)
        except EOFError:
            print("Adieu, adieu, to",p.join(mylist))
            break

    