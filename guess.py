import random
n = random.randint(1,65)
guess = int(input("Enter an integer from 1 to 65: "))
while n != "guess":
    print
    if guess < n:
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 65: "))
    elif guess > n:
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 65: "))
    else:
        print ("you guessed it!")
        break
    print









'''sample outpt 1 to 65:4
sample output you guessed it '''
