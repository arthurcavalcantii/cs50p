#“All vanity plates must start with at least two letters.”
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
#“No periods, spaces, or punctuation marks are allowed.”

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) in range(2,7):
        s1 = list(s)
        s2 = str(s1[0])
        s2_ = str(s1[1])
        s3 = s2.isalpha()
        s3_ = s2_.isalpha()
        if s3 == True and s3_ == True:
            return True
main()
            


