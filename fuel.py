def main():
    num = get_percentage()
    if num <= 1:
        print("E")
    elif num >= 99:
        print("F")
    else:
        print(f"{num}%")

def get_percentage():
    while True:
        try:
            fraction = input("Fraction: ").split("/")
            x = int(fraction[0])
            y = int(fraction[1])
            if x <= y:
                z = x / y
                percentage = round(z * 100)
                return percentage
        except (ValueError, ZeroDivisionError):
            pass

main()


