def int_check(question, blank, error="basic", bigger_than=0, exit_enabled="no"):
    """Checks if the user has entered an integer"""

    if error == "basic":
        error = "Please enter an integer that is bigger than zero."

    while True:

        response = input(question)

        if exit_enabled == "yes" and response == "xxx":
            return response

        if response == "":
            return blank

        try:
            response = int(response)
            if response <= bigger_than:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


user_ans = int_check("How many Rounds? ", "infinite")
print(user_ans)
