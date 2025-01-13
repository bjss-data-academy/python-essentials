# For ... range
for count in range (3):
    print( "Repeat number", count )


for count in range(1,6):
    print("Counting between 1 aand 5 inclusive", count)

# while loop
word = input ("Type a word, or type 'quit' to end: ")
while word != "quit":
    print("you typed", word)
    word = input ("Type a word, or type 'quit' to end: ")

# continue
for i in range(6):
    if i == 4:
        continue

    print("continue", i)

# break
for i in range(666):
    if i == 4:
        break

    print("break", i)

print("break took us out of the loop without completing it")