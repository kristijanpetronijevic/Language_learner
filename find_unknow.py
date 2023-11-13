import json
import random
from colorama import Fore, Style

if __name__ == '__main__':
    path = '/Users/kriskasira/Documents/Language_learner/train100.json'

    with open(path, 'r') as f:
        dict_data = json.load(f)

    iterations = 30
    mistake_dict = {}
    print('Unesi 1 ako znas ili 0 ako ne znas rec!')
    i = 0
    for word in dict_data:
        if i >= iterations:
            break
        i = i + 1
        print(word)
        cond = int(input())
        if cond == 0:
            mistake_dict[word] = dict_data[word]

    out_name = 'mistake_list1.json'

    try:
        with open(out_name, 'r') as o:
            existing_data = json.load(o)
    except FileNotFoundError:
        existing_data = {}

    existing_data.update(mistake_dict)

    with open(out_name, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, indent=2)
