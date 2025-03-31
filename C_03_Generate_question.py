import random


def generate_equation(digits):
    question = []
    num_list = []
    operations_chosen = []
    nums = 0
    operation = "+"
    while nums < digits:
        num = random.randint(1, 9)
        nums += 1
        num_list.append(num)
        question.append(num)
        if len(operations_chosen) < digits - 1:
            operation = random.choice(operations_list)
            operations_chosen.append(operation)
            question.append(operation)
    if operation == "+":
        fin_equ = f"adding {num_list} together"
        ans = sum(num_list)
    elif operation == "-":
        fin_equ = f"subtracting {num_list[1:]} from {num_list[0]}"
        ans = num_list[0] - sum(num_list[1:])
    else:
        fin_equ = f"multiplying {num_list} together"
        ans = num_list[0] * num_list[1]

    return fin_equ, ans, question


operations_list = [
    "+",
    "-",
    "*",
]

# Main code
gen_equ = generate_equation(3)
print(gen_equ[0])
print(gen_equ[1])
print(gen_equ[2])
