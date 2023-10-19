import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 5
COLOR_LENGTH = 4

def generate_color_code():
    code = []
    
    for _ in range(COLOR_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    
    return code



def make_guess():
    while True:
        guess = input("Guess: ").upper().split(" ")
        
        if len(guess) != COLOR_LENGTH:
            print(f"You must guess {COLOR_LENGTH} length of colors.")
            continue
        
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}.... Try Again.")
                break
        
        else:
            break
    
    return guess



def check_guess(guess, real_color):
    colors_count = {}
    correct_pos = 0
    incorrect_pos = 0
    
    for color in real_color:
        if color not in colors_count:
            colors_count[color] = 0
        colors_count[color] +=1
        
    for guess_color, true_color in zip(guess, real_color):
        if guess_color == true_color:
            correct_pos +=1
            colors_count[guess_color] -=1
        
    for guess_color, true_color in zip(guess, real_color):
        if guess_color in colors_count and colors_count[guess_color] > 0:
            incorrect_pos +=1
            colors_count[guess_color] -=1
            
    return correct_pos, incorrect_pos



def game():
    print(f"Welcome to MASTERMIND GAME. You have {TRIES} tries to guess the colors...")
    print(f"In every guesses, guess {COLOR_LENGTH} colors.Valid colors:", *COLORS)
    
    color_code = generate_color_code()
    for attemp in range(1, TRIES + 1):
        guess = make_guess()
        correct_pos, incorrect_pos = check_guess(guess, color_code)
        
        if correct_pos == COLOR_LENGTH:
            print(f"You have guessed right in {attemp} tries.Congratulation..")
            break
        print(f"Correct position: {correct_pos} | Incorrect position: {incorrect_pos}")
        
    else:
        print(f"You ran out of tries. The real code was: ", *color_code)
        
    
    
    
if __name__ == "__main__":
    while True:
        game()
        
        ans = input("\nDo you wanna play again...(y/n): ").lower()
        print("\n")
        if ans != 'y':
            break
    
        
        