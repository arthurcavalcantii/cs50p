
def main():
    user_input = (input("Greeting: ").casefold().strip())
    print (value(user_input))

def value(greeting):
    greeting1 = list(greeting)
    if greeting1 [0] == "h" and greeting1 [1] == "e" and greeting1 [2] == "l" and greeting1 [3] == "l" and greeting1 [4] == "o":
        return "$0"
    elif greeting != "hello" and greeting [0] == "h":
        return "$20"
    if greeting1[0] != "h":
        return "$100"

if __name__ == "__main__":
    main()