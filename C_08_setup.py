def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a value from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it is lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item
            # check if the user response
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something valid
        print(error)
        print()


def int_check(question, error, smaller_than, bigger_than, exit_enabled="no"):
    """Checks if the user has entered an integer"""

    while True:

        response = input(question)

        if exit_enabled == "yes" and response == "xxx":
            return response

        try:
            response = int(response)
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


instructions = {
    "These are the instructions"
}
# Main code
# asks if user wants instructions
want_instructions = string_checker("Do you want to see instructions? ")
if want_instructions == "yes":
    print(instructions)

# Sets up the amount of digits per question for the game

digit_amount = int_check("How many digits do you want in each question? ", "Please enter an integer from 1 to 5.", 5, 1, "no")
print(digit_amount)
