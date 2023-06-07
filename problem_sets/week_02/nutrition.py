# Nutrition Facts

# In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

# Hints
# Rather than use a conditional with 20 Boolean expressions, one for each fruit, better to use a dict to associate a fruit with its calories!
# If k is a str and d is a dict, you can check whether k is a key in d with code like:
# if k in d:
# ...
# Take care to output the fruit’s calories, not calories from fat!

# ------------------------------------------------------------------------------------

# User inputs a fruit (case-insensitively)
# Outputs the number of calories in one portion of that fruit

# Dictionary keys are `fruit` and `calories`. Values are fruit name and its calories
fruits = [
    {"fruit": "apple", "calories": 130},
    {"fruit": "avocado", "calories": 50},
    {"fruit": "banana", "calories": 110},
    {"fruit": "cantaloupe", "calories": 50},
    {"fruit": "grapefruit", "calories": 60},
    {"fruit": "grapes", "calories": 60},
    {"fruit": "honeydew", "calories": 50},
    {"fruit": "kiwifruit", "calories": 90},
    {"fruit": "lemon", "calories": 15},
    {"fruit": "lime", "calories": 20},
    {"fruit": "nectarine", "calories": 60},
    {"fruit": "orange", "calories": 80},
    {"fruit": "peach", "calories": 60},
    {"fruit": "pear", "calories": 100},
    {"fruit": "pineapple", "calories": 50},
    {"fruit": "plums", "calories": 70},
    {"fruit": "strawberries", "calories": 50},
    {"fruit": "sweet cherries", "calories": 100},
    {"fruit": "tangerine", "calories": 50},
    {"fruit": "watermelon", "calories": 80},
]


def main():
    fruit = input("Item: ").lower()
    calories = get_calories(fruit)

    # Conditional checks if `get_calories` returned a calorie count (aka not `None`), then prints the calories
    if calories is not None:
        print("Calories:", calories)
    else:
        print("", end="")


# This function iterates over the list of fruits. For each fruit, it checks if the "fruit" value matches the `fruit_name` passed into the function. If match is found, it returns the associated number of calories. If no match is found after checking all the fruits, it returns `None` to indicate that the user inputted fruit is not in the list of dicts
def get_calories(fruit_name):
    for x in fruits:
        if x["fruit"] == fruit_name:
            return x["calories"]
    return None


main()
