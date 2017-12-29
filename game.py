import random


#ability to play again

def game():
    #generate a random number between 1 and 10
    secret_num = random.randint(1, 10)
    guesses = []
    #get a number guess from player
    while len(guesses) < 5:
        #safely make an int
        try:
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("That is not a number.")    
        else:    
            #compare guess with random number and print hit or miss
            if guess == secret_num:
                print("Correct! The number was {}.".format(secret_num))
                break
            elif guess < secret_num:
                print("A little bit higher")  
            else:
                print("That was a little too high. Try again, please.")   
            guesses.append(guess)    
    else:
        print("You didn't get it. My number was {}".format(secret_num))
    play_again = input("Do you want to play again? Y/n ") 
    if play_again.lower() != 'n':
        game()
    else:
        print("Goodbye!")       
game()                 

