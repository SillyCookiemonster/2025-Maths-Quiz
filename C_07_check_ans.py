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

    # calculates question and answer depending on 'level' (amount of digits)
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


def int_check(question, error, exit_enabled="no"):
    """Checks if the user has entered an integer"""

    while True:

        response = input(question)

        if exit_enabled == "yes" and response == "xxx":
            return response

        if response == "":
            return error

        try:
            response = int(response)
            return response

        except ValueError:
            print(error)


operations_list = [
    "+",
    "-",
    "*",
]

# Main code
# gets equation and answer and prints it
gen_equ = generate_equation(3)
question_output = f"{gen_equ[0]} = "
solution = gen_equ[1]
user_ans = int_check(question_output, "Please enter an integer.", "yes")
if user_ans == solution:
    print(f"Correct! The answer was {solution}")
elif user_ans == "xxx":
    print("you have exited the program!")
else:
    print(f"Wrong! The answer was {solution}")
