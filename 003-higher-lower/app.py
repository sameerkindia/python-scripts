from data import celebrities
import random

def format_data():
      pass

option_a = random.choice(celebrities)
option_b = random.choice(celebrities)

if option_a == option_b:
   option_b = random.choice(celebrities)
       

user_points = 0
is_game_on = True





while is_game_on:
    print(f"Option A. {option_a["name"]} {option_a['profession']} {option_a['country']}")
    print(f"Option B. {option_b["name"]} {option_b['profession']} {option_b['country']}")

    user_input = input("who has more followers?` A or B : ").lower()

    if user_input == "a" and option_a["followers"] > option_b["followers"] :
            print("")
            print(f"{option_a["name"]} has {option_a['followers']}")
            print(f"{option_b["name"]} has {option_b['followers']}")
            print("")
            user_points += 1
        #     option_a = option_b
            option_b = random.choice(celebrities)
    elif user_input == "b" and option_a["followers"] < option_b["followers"]:
            print("")
            print(f"{option_a["name"]} has {option_a['followers']}")
            print(f"{option_b["name"]} has {option_b['followers']}")
            print("")
            user_points += 1
            option_a = option_b
            option_b = random.choice(celebrities)
    else:
            print(f"{option_a["name"]} has {option_a['followers']}")
            print(f"{option_b["name"]} has {option_b['followers']}")
            print("")
            print(f"You lose! Your points :- {user_points}")
            is_game_on = False
