# import random

# movies_list = ['jawan', 'dunki', 'superman', 'ironman']

# random_movie = movies_list[random.randrange(0, len(movies_list))]
# print(random_movie)

# user_life = 5
# isWordGuessed = False
# user_inputs_arr = []

# while user_life > 0:
#     print(user_life , " this is user life")
#     user_input = input('Guess a word : ')
#     if random_movie.find(user_input):
#         # user_inputs_arr.extend(user_input)
#         print(random_movie.find(user_input) , " this is movie found")
#     else:
#         print("you are wrong")
#         user_life -= 1
#         print(user_life , " this is user life")


# # Solution 1
# import random

# movies_list = ['jawan', 'dunki', 'superman', 'ironman']

# random_movie = random.choice(movies_list)

# print(random_movie)

# movies_letter = []

# guess = input("Guess a letter : ").lower()

# for int, letter in enumerate(random_movie):
#     if letter == guess:
#         movies_letter.append(letter)
#     else:
#         movies_letter.append('_')

# print(movies_letter)
