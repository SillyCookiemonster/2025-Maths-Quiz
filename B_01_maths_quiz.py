import random


def generate_equation(digits):
    """Generates question and answer according to the amount of digits required"""
    raw_var = []
    num_list = []
    operations_chosen = 0
    nums = 0

    # keep generating digits and operations depending on the level
    while nums < digits:
        num = random.randint(1, 9)
        nums += 1
        num_list.append(num)
        raw_var.append(num)

        # generate operations depending on 'level'
        if operations_chosen < digits - 1:
            operation = random.choice(operations_list)
            raw_var.append(operation)
            operations_chosen += 1

    # calculates question and answer depending on amount of digits
    if digits == 2:
        fin_equ = f"{raw_var[0]} {raw_var[1]} {raw_var[2]}"

    elif digits == 3:
        fin_equ = f"{raw_var[0]} {raw_var[1]} {raw_var[2]} {raw_var[3]} {raw_var[4]}"

    elif digits == 4:
        fin_equ = f"{raw_var[0]} {raw_var[1]} {raw_var[2]} {raw_var[3]} {raw_var[4]} {raw_var[5]} {raw_var[6]}"

    else:
        fin_equ = f"{raw_var[0]} {raw_var[1]} {raw_var[2]} {raw_var[3]} {raw_var[4]} " \
                  f"{raw_var[5]} {raw_var[6]} {raw_var[7]} {raw_var[8]}"
    ans = eval(fin_equ)

    return fin_equ, ans


def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a value from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it is lowercase
        user_reply = input(question).lower()

        for i in valid_ans:
            # check if the user response is a word in the list
            if i == user_reply:
                return i
            # check if the user response
            # is the first letter of an item in the list
            elif user_reply == i[0]:
                return i

        # print error if user does not enter something valid
        print(error)
        print()


def int_check(question, error, smaller_than, bigger_than, exit_enabled="no"):
    """Checks if the user has entered an integer"""

    while True:
        # Asks user question
        response = input(question)

        if exit_enabled == "yes" and response == "xxx":
            return response

        try:
            response = int(response)
            # check if user response is within boundaries
            if smaller_than == "none":
                if response < bigger_than:
                    print(error)
                else:
                    return response
            else:
                if response < bigger_than or response > smaller_than:
                    print(error)
                else:
                    return response

        except ValueError:
            print(error)


# Operations the questions can have
operations_list = [
    "+",
    "-",
    "*",
]

game_history = []

instructions = '''***** Instructions *****

To begin, choose the amount of digits you want in the question.

Then you can start to answer the questions!
Remember that negative answers can be allowed.

Enter <xxx> to exit during a question.

Happy answering!
    '''


# Main code
# Variable setup
round_num = 0

# Title
print("==== Maths Quiz ====")

# asks if user wants instructions
want_instructions = string_checker("Do you want to see instructions? ")
if want_instructions == "yes":
    print(instructions)

# Asks user how many digits they want for each question
digit_amount = int_check("How many digits do you want in each question? ", "Please enter an integer between 2 and 5.", 5, 2,
                         "no")

# Rounds
while True:
    round_num += 1
    # gets equation and answer
    gen_equ = generate_equation(digit_amount)
    fin_q = gen_equ[0]
    true_ans = gen_equ[1]

    # asks user to answer the question
    # the parameters are the lowest and highest possible answer to specific randomly generated questions
    user_response = int_check(f"{gen_equ[0]} = ", "Please enter an integer between -6561 and -59050.", 59050, -6561,
                              "yes")

    # gives the user feedback on their answer
    if user_response == "xxx":
        break
    elif user_response == true_ans:
        print("Correct!")
    else:
        print(f"Incorrect! The answer was {true_ans}")

    # Record the round that just happened and add it to a list
    if user_response == true_ans:
        game_results = (f"Round {round_num}: Question: {fin_q} | User answered: {user_response}"
                        f" | The user's answer was correct")
    else:
        game_results = (f"Round {round_num}: Question: {fin_q} | User answered: {user_response}"
                        f" | The user's answer was incorrect | The real answer was {true_ans}")
    game_history.append(game_results)

# if the user hasn't played at all and there is no history
# tell them they chickened out
if round_num == 1:
    print("You chickened out!")
    pass
else:
    # if user wants to see history, output the history
    see_history = string_checker("Do you want to see the game history? ")
    if see_history == "yes":
        print("Game History")

        for item in game_history:
            print(item)
