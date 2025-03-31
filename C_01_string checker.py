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


# Main code

want_instructions = string_checker("Do you want to see instructions? ")
print("You chose: ", want_instructions)
