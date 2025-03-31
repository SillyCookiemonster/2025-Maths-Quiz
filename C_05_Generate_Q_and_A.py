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
        ans = eval(f"{raw_var[0]} {raw_var[1]} {raw_var[2]}")

    elif digits == 3:
        fin_equ = f"{raw_var[0]} {raw_var[1]} {raw_var[2]} {raw_var[3]} {raw_var[4]}"
        ans = eval(f"{raw_var[0]} {raw_var[1]} {raw_var[2]} {raw_var[3]} {raw_var[4]}")

    elif digits == 4:
        fin_equ = f"{raw_var[0]} {raw_var[1]} {raw_var[2]} {raw_var[3]} {raw_var[4]} {raw_var[5]} {raw_var[6]}"
        ans = eval(f"{raw_var[0]} {raw_var[1]} {raw_var[2]} {raw_var[3]} {raw_var[4]} {raw_var[5]} {raw_var[6]}")

    else:
        fin_equ = f"{raw_var[0]} {raw_var[1]} {raw_var[2]} {raw_var[3]} {raw_var[4]} {raw_var[5]} {raw_var[6]} {raw_var[7]} {raw_var[8]}"
        ans = eval(f"{raw_var[0]} {raw_var[1]} {raw_var[2]} {raw_var[3]} {raw_var[4]} {raw_var[5]} {raw_var[6]} {raw_var[7]} {raw_var[8]}")

    return fin_equ, ans


operations_list = [
    "+",
    "-",
    "*",
]

# Main code
# gets equation and answer and prints it
gen_equ = generate_equation(3)
print(gen_equ[0])
print(f"= {gen_equ[1]}")
