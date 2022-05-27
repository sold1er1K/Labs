from model import*
from view import*
from controller import*
import sys


if __name__ == "__main__":
    while True:
        variants = ['GUI', 'CLI']
        print('Commands: GUI, CLI')
        choice = str(input())
        choice = choice.strip()
        if choice == variants[0]:
            model = Model()
            controller = Controller(model)
            Garden(model, controller).run()
            sys.exit()
        elif choice == variants[1]:
            garden = Model()
            print("Вчера")
            garden.show()
            garden.next_day()
            print("Сегодня")
            garden.show()
            command = ['add_bed', 'plant_tree', 'plant_cult', 'watering', 'fertilize', 'kill_pest', 'treatment', 'weeding',
                       'harvesting', 'show', 'exit', 'next_day']
            print(
                'Commands: add_bed, plant_tree, plant_cult, watering, fertilize, kill_pest, treatment, weeding, harvesting, show, exit, next_day')
            while True:
                choice = str(input())
                choice = choice.strip()
                if choice == command[0]:
                    st = garden.add_garden_bed()
                    print(st)
                elif choice.startswith(command[1], 0, -1):
                    tmp = choice.split(" ", 1)
                    st = garden.plant_tree(tmp[1])
                    print(st)
                elif choice.startswith(command[2], 0, -1):
                    tmp = choice.split(" ", 2)
                    st = garden.plant_cultivated_plant(tmp[1], int(tmp[2]) - 1)
                    print(st)
                elif choice.startswith(command[3], 0, -1):
                    tmp = choice.split(" ", 1)
                    st = garden.watering(int(tmp[1]) - 1)
                    print(st)
                elif choice.startswith(command[4], 0, -1):
                    tmp = choice.split(" ", 1)
                    st = garden.fertilize(int(tmp[1]) - 1)
                    print(st)
                elif choice.startswith(command[5], 0, -1):
                    tmp = choice.split(" ", 2)
                    st = garden.kill_pest(tmp[1], int(tmp[2]) - 1)
                    print(st)
                elif choice.startswith(command[6], 0, -1):
                    tmp = choice.split(" ", 2)
                    st = garden.treatment(tmp[1], int(tmp[2]) - 1)
                    print(st)
                elif choice.startswith(command[7], 0, -1):
                    tmp = choice.split(" ", 1)
                    st = garden.weeding(int(tmp[1]) - 1)
                    print(st)
                elif choice.startswith(command[8], 0, -1):
                    tmp = choice.split(" ", 2)
                    st = garden.harvesting(tmp[1], int(tmp[2]) - 1)
                    print(st)
                elif choice == command[9]:
                    print(garden.show())
                elif choice == command[10]:
                    garden.set_data_in_file()
                    sys.exit()
                elif choice == command[11]:
                    garden.next_day()
                    garden.show()
                else:
                    print('WRONG INPUT!')
                garden.set_data_in_file()
        else:
            print('WRONG INPUT!')
