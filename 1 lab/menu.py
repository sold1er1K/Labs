from library import*

commands = ['modeling', 'add bed', 'plant tree', 'plant cult', 'water', 'fertilize', 'kill pest',
            'cure', 'weed', 'harvest', 'show', 'exit', 'next day', 'help']
garden = Garden()


def menu() -> None:
    path = ''
    model = ''
    modeling_type = ''
    savings = False
    command_input = True
    while command_input:
        command = str(input()).strip()
        if len(command) == len(commands[0]) + 6 and command[0:8] == commands[0]:
            if command[9] == '-' and command[12] == '-':
                if command[10] == 'n' or command[10] == 'o' and command[13] == 's' or command[13] == 'u':
                    model = command[9:11]
                    modeling_type = command[12:]
                    command_input = False
        else:
            print("[WARNING] Input format: modeling -n/-o -s/-u")
            print("[INFO] -n = new model, -o = old model")
            print("[INFO] -s = step modeling\n")

    if model == '-n':
        path = 'data.json'
    elif model == '-o':
        path = 'savings.json'
        savings = True
    if modeling_type == '-s':
        garden.get_data_from_file(path)
        if savings is True:
            print("Вчера")
            garden.show()
            garden.next_day()
        modeling()


def modeling() -> None:
    print("Today:")
    garden.show()
    while True:
        garden.show()
        choice = str(input()).strip()
        if choice == commands[1]:
            garden.add_garden_bed()
        elif choice.startswith(commands[2], 0, -1):
            tmp = choice.split(" ", 1)
            garden.plant_tree(tmp[1])
        elif choice.startswith(commands[3], 0, -1):
            tmp = choice.split(" ", 2)
            garden.plant_cultivated_plant(tmp[1], int(tmp[2]) - 1)
        elif choice.startswith(commands[4], 0, -1):
            tmp = choice.split(" ", 1)
            garden.watering(int(tmp[1]) - 1)
        elif choice.startswith(commands[5], 0, -1):
            tmp = choice.split(" ", 1)
            garden.fertilize(int(tmp[1]) - 1)
        elif choice.startswith(commands[6], 0, -1):
            tmp = choice.split(" ", 2)
            garden.kill_pest(tmp[1], int(tmp[2]) - 1)
        elif choice.startswith(commands[7], 0, -1):
            tmp = choice.split(" ", 2)
            garden.treatment(tmp[1], int(tmp[2]) - 1)
        elif choice.startswith(commands[8], 0, -1):
            tmp = choice.split(" ", 1)
            garden.weeding(int(tmp[1]) - 1)
        elif choice.startswith(commands[9], 0, -1):
            tmp = choice.split(" ", 2)
            garden.harvesting(tmp[1], int(tmp[2]) - 1)
        elif choice == commands[10]:
            garden.show()
        elif choice == commands[11]:
            return
        elif choice == commands[12]:
            garden.next_day()
            garden.show()
        elif choice == commands[13]:
            print_info()
        else:
            print('[WARNING] Wrong input. Enter "help" to display information')
        garden.set_data_in_file('savings.json')


def print_information():
    print('[INFO] Command list:')
    print('[INFO] modeling -n/-o -s/-u  --  start modeling(-n = new model, -o = old model, -s = step modeling);')
    print('[INFO] add bed -- creating a new garden bed;')
    print('[INFO] plant tree `tree name` -- plant a new tree(names: яблоня, груша);')
    print('[INFO] plant сult `cult name` -- plant a new cultivated plant(names: картофель, томат, перец);')
    print('[INFO] water `bed number` -- water the bed number `bed number`;')
    print('[INFO] fertilize `bed number` -- fertilize the bed number `bed number`;')
    print('[INFO] plant types: tree, cult')
    print('[INFO] kill pest `plant type` `bed number` -- kill pests on the `plant type` in the bed number `bed number`;')
    print('[INFO] cure `plant type` `bed number` -- cure the `plant type` in the bed number `bed number`;')
    print('[INFO] weed `bed number` -- weed the bed number `bed number`;')
    print('[INFO] harvest `plant type` `bed number` -- harvest the `plant type` in the bed number `bed number`;')
    print('[INFO] weed `bed number` -- weed the bed number `bed number`;')
    print('[INFO] show -- current state displaying;')
    print('[INFO] next day -- transition to the next day;')
    print('[INFO] exit -- complete the modeling.')


if __name__ == "__main__":
    menu()
