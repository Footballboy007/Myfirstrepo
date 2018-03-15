name = "James"

subjects = ["English","Math","Spanish"]

print ("hello " + name)

for i in subjects:
    print ("one of my classes is " + i)

name = "James"

cars = ["Ferrari","Maclaren","Audi","Ford","BMW"]

for i in cars:
    if i == "BMW":
        print ("My favorite car is " + i)
    elif i == "maclaren":
        print ("The fastest car is a " + i)
    else:
        print ("The best car is " + i)

videoGames = []

while True:
    print ("What Video game do you like? type 'end' to quit")
    answer = input()

    if answer == "end":
        break
    else:
        VideoGames.append(answer)


for i in VideoGames:
    print("one of your favourite Video Games is " + i)
