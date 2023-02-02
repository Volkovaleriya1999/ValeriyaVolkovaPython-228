from random import choice
import json

def get_person():
    name = ''
    tel = ''

    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letter)

    while len(tel) != 10:
        tel += choice(nums)

    person = {
        'name': name,
        'tel': tel
    }
    return person, tel

def write_json(person_dict, num):

    try:
        data = json.load(open('persons.json'))
    except FileNotFoundError:
        data = {}

    data[num] = person_dict
    print(data)

    with open('person.json', 'w') as file:
        json.dump(data, file, indent=2)
    # with open('persons.json', 'w') as f:
    #     json.dump(data, f, indent=2)

for i in range(5):
    write_json(get_person()[0], get_person()[1])


