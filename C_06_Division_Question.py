import random


def generate_equation(digits):
    """Generates question and answer according to the amount of digits required"""
    all_var = []
    num_list = []
    operations_picked = []
    operations_chosen = 0
    nums = 0
    last_op_is_div = False
    operation = "invalid"

    # keep generating digits and operations depending on the level
    while nums < digits:
        num = random.randint(1, 9)
        num_list.append(num)
        all_var.append(num)
        print(f"step {nums}", num_list)

        # generate operations depending on 'level'
        if operations_chosen < digits - 1:
            operation = random.choice(operations_list)
            operations_picked.append(operation)
            # if the last operation picked was division find and choose a factor of the last number
            if last_op_is_div:

                # finds the factor
                factored = find_factors(num_list[-1])
                print(factored)
                print("yes")

                # chooses a new number from the factors available and replaces original number from list
                print(num_list)
                num = random.choice(factored)
                print(num_list)
                num_list[-1] = num
                all_var[-1] = num
                last_op_is_div = False
            if operation == "/":
                last_op_is_div = True
            all_var.append(operation)
            operations_picked.append(operation)
            operations_chosen += 1

        # Adding numbers to list
        nums += 1

    # calculates question and answer depending on 'level' (amount of digits)
    if digits == 2:
        fin_equ = f"{all_var[0]} {all_var[1]} {all_var[2]}"
        ans = eval(f"{all_var[0]} {all_var[1]} {all_var[2]}")

    elif digits == 3:
        fin_equ = f"{all_var[0]} {all_var[1]} {all_var[2]} {all_var[3]} {all_var[4]}"
        ans = eval(f"{all_var[0]} {all_var[1]} {all_var[2]} {all_var[3]} {all_var[4]}")

    elif digits == 4:
        fin_equ = f"{all_var[0]} {all_var[1]} {all_var[2]} {all_var[3]} {all_var[4]} {all_var[5]} {all_var[6]}"
        ans = eval(f"{all_var[0]} {all_var[1]} {all_var[2]} {all_var[3]} {all_var[4]} {all_var[5]} {all_var[6]}")

    else:
        fin_equ = f"{all_var[0]} {all_var[1]} {all_var[2]} {all_var[3]} {all_var[4]} {all_var[5]} {all_var[6]} {all_var[7]} {all_var[8]}"
        ans = eval(f"{all_var[0]} {all_var[1]} {all_var[2]} {all_var[3]} {all_var[4]} {all_var[5]} {all_var[6]} {all_var[7]} {all_var[8]}")

    return fin_equ, ans


def find_factors(to_factor):
    """Finds all factors of a number"""
    all_factors = []

    # find square root of number to be factored so that our loop is efficient.
    stop_raw = to_factor ** 0.5
    stop = int(stop_raw + 1)

    # loop and check each number from one upwards to check if it's a
    # factor.  Stop when we get to the square root of the number (ie: 'half way')
    for item in range(1, stop):
        num_left = to_factor % item
        # If number fits evenly it will add it to the list
        if num_left == 0:
            all_factors.append(item)

            # retrieve the second 'partner' factor as an integer
            partner = to_factor // item

            # only add factor to list if it is not already in the list
            if partner not in all_factors:
                all_factors.append(partner)

    all_factors.sort()

    if len(all_factors) > 1:
        print(f"The factors of {to_factor} are: {all_factors}\n")

    return all_factors


operations_list = [
    "+",
    "-",
    "*",
    "/"
]

# Main code
# gets equation and answer and prints it
gen_equ = generate_equation(3)
print(gen_equ[0])
print(f"= {gen_equ[1]}")
