import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2<= players <=4:
            break
        else:
            print("\nNumber of players should be within (2 - 4)")
    
    else:
        print("\nNot valid . Try again")


d = dict()
for i in range(players):
    d[i] = input(f"Enter Name of {i+1} player: ")


players_scores = [0 for _ in range(players)]
max_score = 50


while max(players_scores) < max_score:
    for player_idx in range(players):
         
        print(f"\n{d[player_idx]}'s turn has started:")
        print(f"\n{d[player_idx]}'s current score is {players_scores[player_idx]}")
        current_score = 0
            
        while True:
            ans = input(f"\nWould you like to roll {d[player_idx]} (y/n)? ")
            if ans != 'y':
                break
            value = roll()
            if value == 1:
                print("You rolled a 1! You get 0 score ! Turn done \n")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}")
                print(f"Your score is {current_score}")
            if current_score >20:
                print("\nYou cannot score more than 20 at on contigious rolling.Take a break")
                break
            
        players_scores[player_idx] += current_score
        print(f"\n{d[player_idx]}'s total score is {players_scores[player_idx]}")
        
        
max_score = max(players_scores)
winnig_idx = players_scores.index(max_score)

print(f"\nCongratulations!!! {d[winnig_idx]}. Your are  the winner!!! Your winnig score is : {max_score}")
        
                