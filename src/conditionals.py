# Basic if and else. Note whitespace used as code block delimiters

favourite_food = "curry"
print ("Your favourite food is", favourite_food)

if favourite_food == "curry":
    print("You have great taste")
else:
    print("You really should try curry")

# Elif example
fruit = "banana"
pet = "dog"

if fruit == "banana":
    print("You like bananas - and that's all that matters")
elif pet == "cat":
    print("You don't like bananas, but do like cats. That's alright then.")
else:
    print("Don't like bananas, don't like cats. You monster")

# logical expressions
fruit = "grape"
snack = "cheese"

if fruit == "grape" and snack == "cheese":
    print("Grapes and cheese! A cheeseboard - what a splendid idea!")
else:
    print("I'd send that cheeseboard back if I were you")
