import random
options = [
    "+",
    "-",
    "*",
]
num1 = random.randint(1, 9)
num2 = random.randint(1, 9)

operation = random.choice(options)

print(num1, operation, num2)
ans = eval(f"{str(num1)} {operation} {str(num2)}")
test = "blah blah"
print(f"{test}")
test = f"{test} rah rah"
print(f"{test}")
