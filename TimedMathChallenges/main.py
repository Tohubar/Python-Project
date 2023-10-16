import random
import time

OPERATORS = ['+','-','*']
MIN_OPERAND = 3
MAX_OPERAND = 10
TOTAL_PROBLEMS = 10

def generate_math_problems():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    exp = str(left) + " "+operator+ " "+ str(right)
    ans = eval(exp)
    
    return exp,ans

wrong =0
print("In this section you will be asked to solve 10 mathematical problems\nafter solving we will provide total time you take to solve all problems\nalso will get number of wrong answer(if occure any)\n\n")
input("Press enter to start the timing")
print("-------------------------------")



start_time = time.time()
for i in range(TOTAL_PROBLEMS):
    exp,ans = generate_math_problems()
    while True:
        guess = input(f"Problem #{i+1}: {exp} = ")
        if guess == str(ans):
            break
        wrong+=1
        print("Ops! Wrong answer! Try Again..")
        
end_time = time.time()



total_time = end_time - start_time
print("--------------------------------")
print(f"Number of wrong answers: {wrong}")
print(f"Total time consumtions: {round(total_time, 2)}seconds")