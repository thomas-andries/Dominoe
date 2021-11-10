scores = input().split()
# put your python code here
lives = 3
points = 0
for score in scores:
    if score == "C":
        points += 1
    elif score == "I":
        lives -= 1
        if lives == 0:
            print("Game over")
            print(points)
            break
else:
    print("You won")
    print(points)
