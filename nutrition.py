
fruits = {
    "apple": 130, "avocado": 50, "banana": 110, "cantaloupe": 50, "honeydewmelon": 50,
    "grapefruit": 60, "grapes": 90, "kiwifruit": 90, "lemon": 15, "lime": 20,
    "nectarine": 60, "orange": 80, "peach": 60, "pear": 100, "pineapple": 50,
    "plums": 70, "strawberries": 45
}

# Prompt the user to enter a fruit
fruit_input = input("Item: ").casefold().strip()

# Check if the entered fruit is in the dictionary
if fruit_input in fruits:
    calories = fruits[fruit_input]
    print("Calories:", calories)






