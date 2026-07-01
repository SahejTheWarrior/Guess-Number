import random

secret=random.randint(1,50)
lives=5

while lives>0:
    guess=int(input("Guess a number between 1 - 50: "))
    
    if guess == secret:
        print("You win!")
    else:
        diff = abs(secret-guess)
        
        if diff >= 20:
            print("Ice cold")
        elif diff >=10:
            print("Cold")
        elif diff >= 5:
            print("Warm")
        else:
            print("Hot")
        
        lives-=1
       
        print("Lives:", end="")
        for i in range(lives):
            print("❤️", end="")
        print()

if lives == 0:
    print("You lose! The secret number was", secret)
        
