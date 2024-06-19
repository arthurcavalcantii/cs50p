
#while i<3:
    #print("meow")
    #i+=1

#for _ in range(3):
    #print("meow")

#while True:
#    number = int(input(""))
 #   if number >0:
  #      break
#only happens when the user input a value bigger than 0, otherwise keeps asking the question
#for i in range(number):
    #print("meow")

#def main():
   # number = get_number()
    #meow(number)

#def get_number():
    #while True:
        #number = int(input("whats the number? "))
        #if number>0:
            #return number

#def meow(n):
    #for _ in range(n):
       #print ("meow")

#students = ["Hermione", "Harry", "Ron"]
#for i in range(len(students)):
    #print(f"{i+1}.", students[i])

#students = {
    #"Hermione": "Gryffindor",
    #"Harry": "Gryffindor",
    #"Ron": "Gryffindor",
    #"Draco": "Slytherin",
#}
#for i in students:
    #print(i, students[i], sep=", ")
#students = [
    #{"name": "Hermione", "house" : "Gryffindor", "patronus" : "Otter"},
    #{"name": "Harry", "house" : "Gryffindor", "patronus" : "Stag"},
    #{"name": "Harry", "house" : "Gryffindor", "patronus" : "Jack Russel terrier"},
    #{"name": "Draco", "house" : "Slytherin", "patronus" : None}
#]
#for student in students:
    #print(student["name"], student["house"], student["patronus"], sep=(", "))

def main():
    print_square(4)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#"*width)

main()














    
