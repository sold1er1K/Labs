from library import*

garden = Garden()


def menu() -> None:
    savings = False
    variants = ['new_model', 'old_model']
    print('Commands: new_model, old_model')
    variant = str(input())
    if variant == variants[0]:
        path = 'data.json'
    elif variant == variants[1]:
        path = 'savings.json'
        savings = True
    else:
        raise ValueError('WRONG INPUT!')

    variants = ['step_modeling', 'unit_tests']
    print('Commands: step_modeling, unit_tests')
    variant = str(input())
    garden.get_data_from_file(path)
    if variant == variants[0]:
        if savings is True:
            print("Вчера")
            garden.show()
            garden.next_day()
        modeling()
    elif variant == variants[1]:
        while True:
            testing()
            choices = ['continue', 'stop']
            print('Commands: continue, stop')
            choice = str(input())
            if choice == choices[0]:
                return
            elif choice == choices[1]:
                raise ValueError('WRONG INPUT!')
    else:
        raise ValueError('WRONG INPUT!')


def modeling() -> None:
    print("Сегодня")
    garden.show()
    command = ['add_bed', 'plant_tree', 'plant_cult', 'watering', 'fertilize', 'kill_pest', 'treatment', 'weeding', 'harvesting', 'show', 'exit', 'next_day']
    print('Commands: add_bed, plant_tree, plant_cult, watering, fertilize, kill_pest, treatment, weeding, harvesting, show, exit, next_day')
    while True:
        garden.show()
        choice = str(input())
        choice = choice.strip()
        if choice == command[0]:
            garden.add_garden_bed()
        elif choice.startswith(command[1], 0, -1):
            tmp = choice.split(" ", 1)
            garden.plant_tree(tmp[1])
        elif choice.startswith(command[2], 0, -1):
            tmp = choice.split(" ", 2)
            garden.plant_cultivated_plant(tmp[1], int(tmp[2]) - 1)
        elif choice.startswith(command[3], 0, -1):
            tmp = choice.split(" ", 1)
            garden.watering(int(tmp[1]) - 1)
        elif choice.startswith(command[4], 0, -1):
            tmp = choice.split(" ", 1)
            garden.fertilize(int(tmp[1]) - 1)
        elif choice.startswith(command[5], 0, -1):
            tmp = choice.split(" ", 2)
            garden.kill_pest(tmp[1], int(tmp[2]) - 1)
        elif choice.startswith(command[6], 0, -1):
            tmp = choice.split(" ", 2)
            garden.treatment(tmp[1], int(tmp[2]) - 1)
        elif choice.startswith(command[7], 0, -1):
            tmp = choice.split(" ", 1)
            garden.weeding(int(tmp[1]) - 1)
        elif choice.startswith(command[8], 0, -1):
            tmp = choice.split(" ", 2)
            garden.harvesting(tmp[1], int(tmp[2]) - 1)
        elif choice == command[9]:
            garden.show()
        elif choice == command[10]:
            return
        elif choice == command[11]:
            garden.next_day()
            garden.show()
        else:
            print('WRONG INPUT!')
        garden.set_data_in_file('savings.json')


def testing() -> None:
    pass


menu()
