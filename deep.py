answer = input("What is the Answer to the Great Question of Life, The Universe, and Everything? ").casefold().strip()

if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")