grocery_list = {}

try:
    while True:
        item = input().strip().lower()
        grocery_list[item] = grocery_list.get(item, 0) + 1
except EOFError:
    pass

sorted_list = sorted(grocery_list.items())
#count is the VALUE, item is the KEY
#when using pairs in a for loop, the order is always VALUE THEN KEY
for count, item in sorted_list:
    print(f"{item} {str(count).upper()} ")



