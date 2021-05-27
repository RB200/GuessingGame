import random
randomNumber=random.randint(1,9)
chance = 0 
print('Guess a number between 1 and 9')
while chance<5:
    guess=int(input('Enter your guess:'))
    if guess == randomNumber:
        print('Congrats! You won!')
        break
    elif guess < randomNumber:
        print('Your guess was too low. Guess again')
    else:
        print('Your guess was too high. Guess again')
    chance=chance+1
if not chance <5:
    print('You lose. The number was ', randomNumber)
