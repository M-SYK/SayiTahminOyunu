import random
import time
print("Please enter the number between 1-100: ")
print("You have 5 guesses.")
num = random.randint(1,100)
guess_right=5
while True:
    guess = int(input("Your guess: "))
    if guess==num:
        print("Being checked...")
        time.sleep(1)#1 saniye bekleyerek sonucu gösteriyor.
        print("Congratulations...")
        break
    elif guess>num:
        print("Being checked...")
        time.sleep(1)
        guess_right -=1
        print("Please enter a smaller number.")
        print("Guess right: ",guess_right)
    else:
        print("Being checked...")
        time.sleep(1)
        guess_right -= 1
        print("Please enter a bigger number.")
        print("Guess right: ", guess_right)
    if guess_right==0:
        print("Your guess is over.")
        print("The number is ",num,".")
        break