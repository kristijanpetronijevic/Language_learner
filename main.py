import json
import random
from colorama import Fore, Style

if __name__ == '__main__':
    path = '/Users/kriskasira/Documents/oxford3000/oxford3000.json'

    with open(path, 'r') as f:
        dictionary = json.load(f)

    iterations = 10
    mistake_list = {}

    for _ in range(iterations):
        random_keys = random.sample(list(dictionary.keys()), 5)
        correct = random.choice(random_keys)

        print(Fore.BLUE + f'Prevod engleske reci {correct} je:' + Style.RESET_ALL)
        print("Pomoc:")
        for i, key in enumerate(random_keys, start=1):
            print(f'{i}) {dictionary[key]}', end=' ')
        print()

        answer = input('\nUnesi redni broj odgovora\n')

        if answer not in ['1', '2', '3', '4', '5']:
            print(Fore.RED + 'Greska!' + Style.RESET_ALL)
            break

        if random_keys[int(answer) - 1] == correct:
            print(Fore.GREEN + 'Tacno!' + Style.RESET_ALL)
        else:
            print(Fore.RED + 'Netacno!' + Style.RESET_ALL)
            print(Fore.YELLOW + f"Tacna rec je: {dictionary[correct]}" + Style.RESET_ALL)
            mistake_list[correct] = dictionary[correct]
            print('------------------------------------')

    print("Sledece reci ste pogresili.")
    for key, value in mistake_list.items():
        print(Fore.YELLOW + f"{key}: {value}" + Style.RESET_ALL)

    out_name = 'podaci.json'

    try:
        with open(out_name, 'r') as o:
            existing_data = json.load(o)
    except FileNotFoundError:
        existing_data = []

    existing_data.extend([mistake_list])

    with open(out_name, 'w') as f:
        json.dump(existing_data, f, indent=2)
