import json
import random
from colorama import Fore, Style

if __name__ == '__main__':
    
    #path = input('Unesite fajl za vezbu!\n')

    #path = '/Users/kriskasira/Documents/oxford3000/oxford3000.json'
    #path = '/Users/kriskasira/Documents/Language_learner/mistake_list1.json'
    p = int(input('Unesi 1 za vezbanje greski ili 2 za vezbanje svih reci\n'))
    if p not in [1, 2]:
        print('Neispravan broj!')
        exit()

    if p == 1:
        path = '/Users/kriskasira/Documents/Language_learner/mistake_list1.json'
    else:
        path = '/Users/kriskasira/Documents/oxford3000/oxford3000.json'
    
    with open(path, 'r') as f:
        dict_data = json.load(f)

    iterations = 10
    mistake_dict = {}

    for _ in range(iterations):
        random_keys = random.sample(list(dict_data.keys()), 5)
        correct = random.choice(random_keys)

        print(Fore.BLUE + f'Prevod engleske reci ' + Style.RESET_ALL, end='')
        print(Fore.MAGENTA+ f'{correct} '.upper() + Style.RESET_ALL)
        print("Pomoc:")
        for i, key in enumerate(random_keys, start=1):
            print(f'{i}) {dict_data[key]}', end=' ')
        print()

        answer = input('\nUnesi redni broj odgovora\n')

        if answer not in ['1', '2', '3', '4', '5']:
            print(Fore.RED + 'Greska!' + Style.RESET_ALL)
            break

        if random_keys[int(answer) - 1] == correct:
            print(Fore.GREEN + 'Tacno!' + Style.RESET_ALL)
        else:
            print(Fore.RED + 'Netacno!' + Style.RESET_ALL)
            print(Fore.YELLOW + f"Tacna rec je: {dict_data[correct]}" + Style.RESET_ALL)
            mistake_dict[correct] = dict_data[correct]
            print('------------------------------------')

    print("Sledece reci ste pogresili.")
    for key, value in mistake_dict.items():
        print(Fore.YELLOW + f"{key}: {value}" + Style.RESET_ALL)

    out_name = 'mistake_list.json'

    try:
        with open(out_name, 'r') as o:
            existing_data = json.load(o)
    except FileNotFoundError:
        existing_data = {}

    existing_data.update(mistake_dict)

    with open(out_name, 'w') as f:
        json.dump(existing_data, f, indent=2)
