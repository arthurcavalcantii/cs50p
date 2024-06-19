def main():
    answer = input("What time is it? ")
    time = convert(answer)
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")

def convert(n):
    hours, minutes = n.split(":")
    converted_minutes = float(minutes) / 60
    converted_hours = float(hours)
    return converted_hours + converted_minutes

if __name__ == "__main__":
    main()
