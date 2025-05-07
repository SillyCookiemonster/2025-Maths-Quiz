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


user_ans = int_check("How many Digits? ", "Please enter an integer that is bigger than zero.")
print(user_ans)
