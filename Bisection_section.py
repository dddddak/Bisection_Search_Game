# Guess number what you are thinking (0 to 100)

low = 0
high = 100
num_guess = 0

print("***Think of one number between 0 to 100***")

while True :
    guess = int((high - low) / 2 + low)
    print("Is the number", str(guess) + "?")
    ans = str(input("High: h, Low: l, Correct: c\n"))
    if (ans == 'h') :
        low = guess
        if low <= 0:
            low = 0
    elif (ans == 'l') :
        high = guess
    elif (ans == 'c') :
        print("\n***The number is", str(guess) + "***", "\nThank you for playing\n")
        break
    else :
        print("Try again\n")




