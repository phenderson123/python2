import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print "Roll them dices man..."
    print "The numbers are...."
    print random.randint(min, max)
    print random.randint(min, max)

    roll_again = raw_input("Roll em again dude?")
