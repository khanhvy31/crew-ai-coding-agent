import random
import json

def rock_paper_scissors(num_rounds):
    choices = ['rock', 'paper', 'scissors']
    results = {'player1': 0, 'player2': 0, 'ties': 0}

    for _ in range(num_rounds):
        player1_choice = random.choice(choices)
        player2_choice = random.choice(choices)

        if player1_choice == player2_choice:
            results['ties'] += 1
        elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
             (player1_choice == 'paper' and player2_choice == 'rock') or \
             (player1_choice == 'scissors' and player2_choice == 'paper'):
            results['player1'] += 1
        else:
            results['player2'] += 1

    return results

num_rounds = 10  # You can change this to any number of rounds required.
outcome = rock_paper_scissors(num_rounds)
print(outcome)

# Save the outcome to a JSON file
with open('outcome.json', 'w') as json_file:
    json.dump(outcome, json_file)