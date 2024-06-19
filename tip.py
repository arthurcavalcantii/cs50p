def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #tirar o dolar, 1 casa decimal
    d1 = d.replace("$", "")
    return float(d1)

def percent_to_float(p):
    #tirar o porcento, transformar o valor de porcentagem em decimal (50% ----> 50 ----> 0.5)
    p1 = p.replace("%", "")
    p2 = float(p1) / 100
    return float(p2)

main()