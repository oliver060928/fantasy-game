import inquirer
import random
import time
class Item:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Player:
    def __init__(self, name, armor, health, strength, backpack: [Item]):
        self.name = name
        self.armor = armor
        self.health = health
        self.strength = strength
        self.backpack = backpack

class Enemy:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength



def exists_in_backpack(player, id):
    for item in player.backpack:
        if item.id == id:
            return True
    return False

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

def event_1(player):
    questions = [
        inquirer.List('result',
                      message="Welcome, choose your character",
                      choices=["Bob", "Dylan"])
    ]
    answer = inquirer.prompt(questions)

    player.name = answer["result"]
    event_2(player)

def event_2(player):
    choice1 = "Go left"
    choice2 = "Go right"
    questions = [
        inquirer.List('result',
                      message="Hi {}, I am your guide".format(player.name),
                      choices=[choice1, choice2])
    ]
    answer = inquirer.prompt(questions)

    if answer["result"] == choice2:
        event_3(player)
    else:
        event_4(player)

def event_3(player):
    choice1 = "go there and see"
    choice2 = " turn around and go to right"
    questions = [
        inquirer.List('result',
                      message="you see a witch house",
                      choices=[choice1, choice2])]

    answer = inquirer.prompt(questions)


def event_4(player):
    choice1 = "go through the forest"
    choice2 = "find another way around the forest"
    questions = [
        inquirer.List('result',
                      message="you see a village behind a forest",
                      choices=[choice1, choice2])]

    answer = inquirer.prompt(questions)

    if answer["result"] == choice2:
        event_5(player)
    else:
        event_(player)

def event_5(player):
    choice1 = "go to the village"
    choice2 = "go in the mine"
    questions = [
        inquirer.List('result',
                      message="you see a mine",
                      choices=[choice1, choice2])]


    answer = inquirer.prompt(questions)

    if answer["result"] == choice2:
        event_6(player)
    else:
        event_(player)

def event_6(player):
    choice1 = "take it up"
    choice2 = "leave it"
    questions = [
        inquirer.List('result',
                      message="it is a key in front of you",
                      choices=[choice1, choice2])]

    answer = inquirer.prompt(questions)

    if answer["result"] == choice1:
        key = Item("key", "key")
        player.backpack.append(key)
    event_7(player)


def event_7(player):
    choice1 = "leave the mine"
    choice2 = "search more"
    questions = [
        inquirer.List('result',
                      message="its a sign on the wall that says maybe it is danger or it is treasure",
                      choices=[choice1, choice2])]

    answer = inquirer.prompt(questions)

    if answer["result"] == choice2:
        event_9(player)
    else:
        event_(player)

def event_9(player):
    choice1 = "leave the mine now"
    choice2 = "open the chest"
    questions = [
        inquirer.List('result',
                      message="you found a chest",
                      choices=[choice1, choice2])]

    answer = inquirer.prompt(questions)

    if answer["result"] == choice2:
        if exists_in_backpack(player, "key"):
            print("you opened the chest")
            event_10(player)
            return
        else:
            print("you don't have a key")
    event_11(player)

def event_10(player):
    choice1 = "leave the mine now"
    choice2 = "open the chest"
    questions = [
        inquirer.List('result',
                      message="in the chest you find ",
                      choices=[choice1, choice2])]







def event_(player):
    choice1 = "go to the village"
    choice2 = "go back to start"
    questions = [
        inquirer.List('result',
                      message="now you are out of the mine",
                      choices=[choice1, choice2])]

    answer = inquirer.prompt(questions)




def event_(player):
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

    event_(player)

def event_(player):
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

    troll = Enemy("Troll", 5, 1)
    result = fight(player, troll, playerStartsFight)

    if result == False:
        print("You died")
    else:
        choice1 = "pick it up"
        choice2 = "leave it"
        questions = [
            inquirer.List('result',
                          message="the troll dropped a key when it died",
                          choices=[choice1, choice2])]
        answer = inquirer.prompt(questions)




player = Player("", 0, 10, 1, [])
event_1(player)











