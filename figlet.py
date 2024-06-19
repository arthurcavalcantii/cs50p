from pyfiglet import Figlet
import sys
import random
figlet = Figlet()
fonts = figlet.getFonts()
user_input = input("Input: ")

if len(sys.argv) == 2:
    sys.exit("Invalid usage")
if len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(user_input))
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
     figlet.setFont(font=random.choice(figlet.getFonts()))
     print(figlet.renderText(user_input))



