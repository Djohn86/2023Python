import json
from random import choice


def get_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nums)

    person = {
        'name': name,
        'tel': tel
    }
    return person, tel


def write_json(person_dict, index):
    try:
        data = json.load(open('newfile.json'))
    except FileNotFoundError:
        data = {}

    data[index] = person_dict
    with open('newfile.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(10):
    write_json(get_person()[0], get_person()[1])
