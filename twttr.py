def main(name):
    print("Output: ", shorten(name), sep="")

def shorten(word):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for letter in vowel:
        word = str(word.replace(letter, ""))

    return word

# Example usage
input_name = input("Input: ")
main(input_name)

    




