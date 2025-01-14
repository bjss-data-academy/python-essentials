# Tuple
favouriteFoods = ("eggs", "sausage", "chips", "beans")
print(favouriteFoods)

# Indexing tuple elements
favouriteFoods = ("eggs", "sausage", "chips", "beans")
print(favouriteFoods[0])
print(favouriteFoods[1])
print(favouriteFoods[2])
print(favouriteFoods[3])

# Unpacking
favouriteFoods = ("eggs", "sausage", "chips", "beans")
(foodA, foodB, foodC, foodD) = favouriteFoods
print("unpacked:", foodA, foodB, foodC, foodD)

# Iteration over tuple
favouriteFoods = ("eggs", "sausage", "chips", "beans")
for food in favouriteFoods:
    print("Iterate tuple:", food)


# List
users = ["alan", "beth", "chris"]
print(users)

# Iterate list
users = ["alan", "beth", "chris"]

for user in users:
    print("Iterate list:", user)

# List CRUD - create list
users = ["alan", "beth", "chris"]
print("Original list:", users)

# Read list element by zero based index
firstUser = users[0]
print("read by index", firstUser )

# Read Negative index counts from end of list
lastUser = users[-1]
print("read by negative index", lastUser)

# Update element value
users[1] = "barry"
print( "Modify list element", users[1])

# Delete element by index
users = ["alan", "beth", "chris"]
users.pop(1) 
print("delete (index)", users)

# Delete element by value
users = ["alan", "beth", "chris"]
users.remove("alan") 
print("delete (value)", users)

# Delete by value removes only first value
users = ["alan", "beth", "chris", "alan"]
users.remove("alan") 
print("delete (first value)",users)

# Delete last element
users = ["alan", "beth", "chris"]
users.pop() 
print("delete last element", users)

# Append element to end
users = ["alan", "beth", "chris"]
users.append("danielle")
print("append", users)

# Join lists
users = ["alan", "beth", "chris"]
new_users = ["dave", "erica"]
updated_users = users + new_users
print("join lists", updated_users)

# List comprehension
users = ["alan", "aaron", "alicia", "beth", "chris"]
users_shard_a = [u for u in users if u.startswith("a")]
print("List comprehension", users_shard_a)
