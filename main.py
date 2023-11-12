import json
import random 
from colorama import Fore, Style


path = '/Users/kriskasira/Documents/oxford3000/oxford3000.json'

with open(path, 'r') as f:
    dict = json.load(f)
    while(1):
        random_keys = random.sample(list(dict.keys()), 5)
        correct = random.choice(random_keys)
        print(Fore.BLUE + f'Prevod engleske reci {correct} je:' + Style.RESET_ALL)
        print("Pomoc:")
        i = 1
        for key in random_keys:
            print(f'{i}) {dict[key]}', end=' ')
            i = i + 1
        answer1 = input('\nUnesi redni broj odgovora\n')
        if answer1 not in ['1', '2' ,'3', '4', '5']:
            print('Greska!')
            break
        answer = int(answer1)
        if random_keys[answer-1] == correct:
           print(Fore.GREEN + 'Tacno!' + Style.RESET_ALL)

        else:
            print(Fore.RED + 'Netacno!' + Style.RESET_ALL)
            print(Fore.YELLOW + f"Tacna rec je: {dict[correct]}" + Style.RESET_ALL)
            print('------------------------------------')


