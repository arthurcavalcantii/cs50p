import contextlib
def main():
    x = get_percentage()
    if x <= 1:
        print("E")
    elif x >= 99:
        print("F")
    else:
        print(f"Fraction: {x}%")

def get_percentage():
    while True:
        with contextlib.suppress(ValueError, ZeroDivisionError):
            fraction = list(input("Fraction: "))
            x = int(fraction[0])
            y = int(fraction[2])
            if x > y:
                continue
            z = x / y
            return round(z * 100)
main()