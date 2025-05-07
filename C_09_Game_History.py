# Initialize list to hold game history
game_history = []

# get data (for testing purposes)
while True:
    rounds_played = input("Round? ")
    if rounds_played == "":
        break
    question = input("Question: ")
    user_response = input("User answer: ")
    true_answer = input("True answer: ")

    if user_response == true_answer:
        game_results = (f"Round {rounds_played}: Question: {question} | User answered: {user_response}"
                        f" | The user's answer was correct")
    else:
        game_results = (f"Round {rounds_played}: Question: {question} | User answered: {user_response}"
                        f" | The user's answer was incorrect | The real answer was {true_answer}")
    game_history.append(game_results)

    print("Game History")

    for item in game_history:
        print(item)
