# Lecture 45 - Chapter 3 Exercise 1 (NUMBER GUESSING GAME)
winning_number = 17
input_number = int(input("Enter a number: "))
if input_number==winning_number:
    print("YOU WIN!!!")
else:
    print("YOU LOSE!!!")
if input_number>winning_number:
    print("Too high")
    if input_number<winning_number:
        print("Too low")
