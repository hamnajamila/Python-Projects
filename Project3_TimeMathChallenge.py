# maths problem challenge
# also calculate time in how much time you solved the ques

import random
import time

operators = ["+", "-", "*"]
min_operand = 3
max_operand = 12
total_ques = 10


def create_challenge():

    # generating rand values for oper, and both the operands
    left = random.randint(min_operand, max_operand) # for left num e.g 2+4 (2 here is on left) and similarly for right as well
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators) # choice picks up random operators from the above list

    expr=str(left) + operator + str(right) # left and right both should gonna be a string 
    answer=eval(expr)
    return expr,answer # return both the expression and its ans


wrong = 0
input("Press any key to start!")


start_time = time.time()

for i in range(total_ques):
    expr, answer = create_challenge()
    while True:
        guess = input("Problem " + str(i + 1) + ": " + expr + " = ") #conv i+1 into a string
        if guess == str(answer):
            break
        else:
           print("Your answer is incorrect! Please Try Again")
        wrong += 1
    

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("Nice work! You finished in", total_time, "seconds!")