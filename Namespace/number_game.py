from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer

def check_number(guess,answer,turns):
    if guess > answer:
        print("Its too high..")
        return turns - 1
    elif guess < answer:
        print("Its too low..")
        return turns - 1
    else:
        print("you got it! The answer was {}".format(answer))

#Make a function to set difficulty

def set_difficulty():
    global turns
    level = input("Choose a difficulty. type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    #Choosing a Random Number between 1 to 100
    print("Welcome to the Number Gussing Game!!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    print(f"Pssst, the correct answer is {answer}")


    turns = set_difficulty()
    

    #Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remianing to guess the number.")
        #Let the user guess a number
        guess = int(input("Make a guess: "))
        #Track the Number of turns and reduce by 1 if they get it wrong
        turns = check_number(guess, answer,turns)
        if turns == 0:
            print("You hav got run out of the attempts")
            return
        elif guess != answer:
            print("Guess again.")




game()








