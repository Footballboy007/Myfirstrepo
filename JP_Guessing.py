import random

number = random.randint(0,3)

words = ["Dog","Cat","House","Golf"]
hint1 = ["Chases cat","Chases mice","Live in","A sport"]
hint2 = ["Animal","Animal","has a roof","Hit a ball in a cup"]

secretword = words[number]
guess = ""
counter = 1

while True:
    print("Guess my seceret word!")
    print("type 'hint1', 'hint2' 'first letter', or 'give up' for answer.")
    guess = input()


    if guess == secretword:
        print("You win!")
        print("It took you" + str(counter) + "guesses.")
        break

    elif guess == "hint1":
        print(hint1[number])

    elif guess == "hint2":
        print(hint2[number])

    elif guess == "first letter":
        print( secretword[0])
        print("You failed" + str(counter) + " times.")
        break

    else:
        print("try again.")
        counter += 1
