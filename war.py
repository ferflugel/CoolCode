# This program calculates the probability of winning an attack at war (boardgame)

import random

def main():
    table = [0, 0] # [attack wins, defense wins]
    attack = int(input("Attack troops: "))
    if attack < 2: # checks for bad input
        print("Invalid attack troops")
        exit()
    defense = int(input("Defense troops: "))
    if defense < 1: # checks for bad input
        print("Invalid defense troops")
        exit()
    sample = 10000
    for i in range(sample):
        result = combat(attack, defense)
        if result == 0:
            table[0] += 1
        else:
            table[1] += 1
    print(f"Simulations: {sample}")
    print(f"Attack chances: {table[0] * 100 / sample}%")
    print(f"Defense chances: {table[1] * 100 / sample}%")

def win_check(at, df): # checks for a winner
    if df == 0: # attack won
        return 0
    elif at == 1: # defense won
        return 1
    else: # no winner
        return 2

def battle(at, df): # simulates a battle
    if at > 4:
        at = 4
    if df > 3:
        df = 3
    at_dices = random.sample(range(1,7), (at - 1))
    at_dices.sort(reverse = True)
    df_dices = random.sample(range(1,7), (df))
    df_dices.sort(reverse = True)
    at_kills = 0
    df_kills = 0
    for j in range(min(len(at_dices), len(df_dices))):
        if(df_dices[j] >= at_dices[j]):
            df_kills += 1
        else:
            at_kills += 1
    result = [df_kills, at_kills]
    return result

def combat(attack, defense): # simulates a whole combat until there is a winner
    at = attack
    df = defense
    while True:
        check = win_check(at, df)
        if check == 0: # attack won
            return 0
        elif check == 1: # defense won
            return 1
        n = battle(at, df)
        at = at - n[0]
        df = df - n[1]

main()
