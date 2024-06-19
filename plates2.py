#“All vanity plates must start with at least two letters.” ####done
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.” ###done
#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
#“No periods, spaces, or punctuation marks are allowed.” ###done

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s): 
    if len(s) not in range(2,7):
        return False
    if not str(s[0]).isalpha() or not str(s[1]).isalpha():
        return False
    if not str(s).isalnum():
        return False
    for char in s:
        if char in [".", " "]:
            return False
    for j in range(len(s) - 1):
        if s[j].isdigit() and s[j+1].isalpha():
            return False
    for i in s:
        if str(i).isdigit():
            return i != '0'
    return True
main()


