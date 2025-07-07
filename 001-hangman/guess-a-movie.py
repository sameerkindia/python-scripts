import random
# import hangman_art from hangman
from hangman import hangman_art
from movies import movies

# movies_list = ['jawan', 'dunki', 'superman', 'ironman']
movies_list = movies


random_movie = random.choice(movies_list).lower()
# random_movie = movies_list[1]

print(random_movie)

movie_length = len(random_movie)

movies_letter = []

for _ in range(movie_length):
    movies_letter.extend('_')

false_guess = []

print(movies_letter)

is_game_over = False

lives = 6

# while not letter == '_' in movies_letter:
while not is_game_over:
    guess = input("Guess a letter : ").lower()
    if guess in movies_letter:
        print(f'you already guessed {guess}')
    
    for position in range(movie_length):
        letter = random_movie[position]

        if letter == guess:
            movies_letter[position] = letter

    print(movies_letter)
    print(hangman_art[lives - 1])

    if guess not in random_movie:
        if guess in false_guess:
            print(f'you already guessed {guess}')
        else:
            false_guess.append(guess)
            lives -= 1

        if lives == 0:
            is_game_over = True
            print("You lose")

    if '_' not in movies_letter:
        is_game_over = True
        print("You Won")
