import random

def guess_the_number():
    while True:
        random_number = random.randint(1, 10)
        
        def user_guess(): 
            while True:
                try:
                    user_input = int(input("Guess a number between 1 and 10: "))
                    return user_input
                except ValueError:
                    print("This is not a valid number. Please enter a valid integer.")
        
        def play_again():
            play_again_input = input("Play again? (Yes/No): ").strip().lower()
            return play_again_input
        
        while True:
            guess = user_guess()
            if guess == random_number:
                print("Correct number!")
                break
            if guess < random_number:
                print("Guess again. Too low")
            if guess > random_number:
                print("Guess again. Too high")
        
        choice = play_again()
        if choice != 'yes':
            break

guess_the_number()
