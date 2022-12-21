import random
n = random.randrange (1,10)
guess = int(input("Enter any number"))
while n!= guess:
    if guess< n:
        print("Too Low")
        guess = int(input("Enter a number again"))
    elif guess > n:
        print("Too low")
        guess = input("Too high")
        guess = int(input("Enter number again"))
    else:
        break
print("You guessed it right !!!")
