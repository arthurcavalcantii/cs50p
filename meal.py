def main():
   original_time = input("What times is it? ")
   hours, minutes = original_time.split(":")
   something = convert(hours, minutes)
   print(something)

def convert(n,x):
    new_n = float(n)
    new_x = float(x)
    final_x = new_x / 60
    return new_n + final_x
    
    
