import time

fruits = 'orange'
name = input("what is your name user:")
print("Welcome " + name, "to the game of hangman")
time.sleep(2)
print("You have five turns to guess the name of the fruit " + name, "!")
time.sleep(3)
guess = " "
turns = 10


while turns > 0:
    failed = 0
    for i in fruits:
        if i in guess:
            print(i, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        print("well done")
        print("The word is: ", fruits)
        break
    user_guess = input("Guess a letter:")
    guess += user_guess

    if user_guess not in fruits:
        turns -= 1
        print("wrong")
        print("you have ", + turns, "more guesses")
if turns == 0:
     print("You lose, LOSER")





