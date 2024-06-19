name = input("Whats your name? ").capitalize()
#if name == "Harry" or name == "Hermione":
    #print ("Griffindor")
#if name == "Draco":
    #print("Slytherin")
#else:
    #print("Who?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print ("Gryffindor")
    case "Draco":
        print ("Slytherin")
    case _:
        print("Who?")