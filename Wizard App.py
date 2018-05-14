import random
import time

from Actors import Wizard, Creature, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print("---------------------")
    print("Wizard Game")
    print("---------------------")


def game_loop():
    creatures = [
        SmallAnimal("Toad", 1),
        Creature("Tiger", 12),
        SmallAnimal("Bat", 3),
        Dragon("Dragon", 50, 75, True),
        Wizard("Evil Wizard", 1000)

    ]

    # print(creatures)

    hero = Wizard("Gandolf", 75)

    while True:

        active_creature = random.choice(creatures)
        print("A {} of level {} has appeared".format(active_creature.name, active_creature.level))
        print()

        cmd = input("Do you [a]ttack, [r]unaway, or [l]ook around? ")
        if cmd == "a":
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("Wizard flees!")
                time.sleep(3)
                print("Wizard returns!")

        elif cmd == "r":
            print("{} flees!".format(hero.name))
        elif cmd == "l":
            print("The wizard {} takes in the surroundings and sees:".format(hero.name))
            for c in creatures:
                print(" * A {} of level {}".format(c.name, c.level))


        else:
            print("Exiting game")
            break

        if not creatures:
            print("You won!")
            break


if __name__ == '__main__':
    main()
