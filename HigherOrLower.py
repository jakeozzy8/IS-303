#VARIABLES
import random
num_guesses = 0
play_again = "Y"
guessed_correctly = False

#While user has pressed "Y"
while play_again == "Y":
    num_guesses = 0
    guessed_correctly = False
    #Computer generates a random number between 1 and 100. 
    secret_number = random.randint(1, 100)

    #while the user has not guessed the number
    while not guessed_correctly:
        # Ask the user to guess a number between 1 and 100 
        number_guess = int(input("Pick a number between 1 and 100: "))
        #While the guess is < 1 or > 100 
        while number_guess < 1 or number_guess > 100 :
                print("Invalid guess! Please try again.")
                number_guess = int(input("Pick a number between 1 and 100: "))
        #   print "Invalid guess! Please try again."

    #Increment the number of guesses
        num_guesses += 1

    # If the guess is > than the number
        if number_guess > secret_number:
            print("Lower!")
        #   Print "Lower!"

        # If the guess is < than the number
        if number_guess < secret_number:
            print("Higher!")
        #   Print "Higher!

        #if the guess is equal to the number
        if number_guess == secret_number:
            print("Congratulations! You guessed the correct number in " + str(num_guesses) + " tries!")
        #   Print "Congratulations! You guessed the correct number in X tries!" where X is the number of guesses.
            guessed_correctly = True
    #loop ends

    #If the number of guesses <= 3
    if num_guesses <= 3:
        print("You are amazing!")
    #   Print "You are amazing!"

    #Else If number of guesses <= 5
    elif num_guesses <= 5:
        print("Impressive!")
    #   Print "Impressive!"

    #Else If number of guesses <= 7
    elif num_guesses <= 7:
        print("Good job!")
    #   Print "Good job!"
    #Else If number of guesses <= 9
    elif num_guesses <= 9:
        print("Took a little longer, but you got it!")
    #   Print "Took a little longer, but you got it!"
    #Else If number of guesses >= 10
    elif num_guesses >= 10:
        print("You need to lock in!")
    #   Print "You need to lock in!"

    #Ask user to press "Y" if they want to play again
    play_again = str(input("Would you like to play again? (Y/N)")).upper()


#loop ends