import json
import random 




path = '/Users/kriskasira/Documents/oxford3000/oxford3000.json'

with open(path, 'r') as f:
    dict = json.load(f)
    while(1):
        random_keys = random.sample(list(dict.keys()), 5)
        correct = random.choice(random_keys)
        print(f'Prevod engleske reci {correct} je:')
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
            print("*********************")
            print("* Odgovor je tacan! *")
            print("*********************")

        else:
            print("*********************")
            print("*  POGRESILI STE!  *")
            print("*********************")
            print(f"Tacna rec je {dict[correct]} ")
        print('------------------------------------')






