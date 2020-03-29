"""A number guessing game.

The computer generates a random, secret integer and the user tries to guess
what the number is. The computer keeps track of the number of guesses from
the user."""
from guess_my_number import Game

def main():
    """Run the guess-my-number game."""
    game = Game()
    guesses = 0

    print("I'm thinking of a number between 1 and " + str(game.upper_bound) + ". \n")
    while True:
        # Ask the user for a guess. If they enter something other than an int,
        # tell them and ask again.
        if guesses != 0:
            print('Number of guesses so far: ' + str(guesses))
        try:
            guess = int(input('Guess the number: '))
            guesses += 1
        except ValueError:
            print('Oops, try entering a number. \n')
            continue

        # Game.check() will return 1 if the guess is too high, -1 if the guess
        # is too low, and 0 if the guess is correct.
        if game.check(guess) == 1:
            print('That guess is too high. \n')
            continue
        if game.check(guess) == -1:
            print('That guess is too low. \n')
            continue
        if game.check(guess) == 0:
            print('Correct! It took you ' + str(guesses) + ' guesses! \n')
            return False

if __name__ == '__main__':
    main()
