import inquirer
import random
import time
class Player:
    def __init__(self, name, armor, health, strength):
        self.name = name
        self.armor = armor
        self.health = health
        self.strength = strength

class Enemy:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength




def fight(player, enemy, playerStrikes=False):
    print("fight!")
    while (player.health > 0 and enemy.health > 0):
        r = random.random()
        if r > 0.5:
            if playerStrikes:
                print("You missed")
            else:
                print("{} missed".format(enemy.name))
        else:
            if playerStrikes:
                enemy.health -= player.strength
                print("You hit {} with {}".format(enemy.name, player.strength))
            else:
                player.health -= enemy.strength
                print("You got hit with {}".format(enemy.strength))

        playerStrikes = (not playerStrikes)
        time.sleep(0.5)
    if player.health > 0:
        return True

    return False


questions = [
    inquirer.List('result',
                  message="Welcome, choose your character",
                  choices=["Bob", "Dylan"])
]
answer = inquirer.prompt(questions)

player = Player(answer["result"], 0, 10, 1)

choice1 = "Go left"
choice2 = "Go right"
questions = [
    inquirer.List('result',
                  message="Hi {}, I am your guide".format(player.name),
                  choices=[choice1, choice2])
]
answer = inquirer.prompt(questions)

if answer["result"] == choice1:

    choice1 = "go through the forest"
    choice2 = "find another way around the forest"
    questions = [
        inquirer.List('result',
                      message="you see a village behind a forest",
                      choices=[choice1, choice2])]

    answer = inquirer.prompt(questions)

    if answer["result"] == choice1:
        choice1 = "put it on"
        choice2 = "leave it"
        questions = [
            inquirer.List('result',
                          message="on your way through the forest you find a leather jacket",
                          choices=[choice1, choice2])]

        answer = inquirer.prompt(questions)

        if answer["result"] == choice1:
            print("Nice")
            player.armor = 3

        choice1 = "go fight the troll"
        choice2 = "find a way around the troll"
        questions = [
            inquirer.List('result',
                          message="you see a troll",
                          choices=[choice1, choice2])]

        answer = inquirer.prompt(questions)

        playerStartsFight = True

        if answer["result"] == choice2:
            print("the troll has caught you")
            playerStartsFight = False

        troll = Enemy("Troll", 10, 2)
        result = fight(player, troll, playerStartsFight)

        if result == False:
            print("You died")
        else:
            choice1 = "go fight the troll"
            choice2 = "find a way around the troll"
            questions = [
                inquirer.List('result',
                              message="you see a troll",
                              choices=[choice1, choice2])]

            answer = inquirer.prompt(questions)
else:
    print("you died")

