import random

randNum  = random.randint(1,100)
print('''***** Hey lets play A game.... You have to Guess a number between 1-100 ....
If You guess it within 7 guess, you are the winner *****''')
guesses = 0

while True:
    userGuess = int(input("Enter your Guess: "))
    guesses += 1
    if(userGuess == randNum):
        print("You guessed it right!")
        print(f"you take {guesses} guesses to make the perfect guess!")
        break
    else:
        
        if userGuess > randNum :
            print("You guessed it wrong! Enter a samller number!")
        else:
            print('You guessed it wrong! Enter a higher number!')

with open('hiscore.txt','r') as f:
    hiscore = int(f.read())

if guesses < hiscore:
    print("You have just broken the highscore!!!")
    with open('hiscore.txt','w') as f:
        f.write(str(guesses))