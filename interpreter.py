#a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place.
#Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:
#x is an integer, y is +, -, *, or /, z is an integer
inicial_input = input("").split()
x = inicial_input[0]
y = inicial_input[1]
z = inicial_input[2]

new_x = float(x)
new_z = float(z)

match y:
    case "+":
        new_x + new_z
    case "-":
        new_x - new_z
    case "*":
        new_x * new_z
    case "/" if new_z != 0:
        new_x / new_z
    case "/" if new_z == 0:
        print("undefined")
    