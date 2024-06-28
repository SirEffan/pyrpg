from lib.environment import Environment
from lib.character import Player
from lib.container import Object, Weapon
from lib.templates.shop import Shop

player = Player("Vex")

beach = Environment("Beachy Forest")
beach.set_text("You've got to a beach and you see trees in the horizon.")

forest = Environment("Forest")
forest.set_text("you're at the forest!")

right = Environment("Right")

left = Environment("Left")

@forest.command("Go Left")
def left():
    print("going Left")
    left.show_menu()

@forest.command("Go Right")
def right():
    print("going Right")
    right.show_menu()

@beach.command("Go To Forest")
def gotoforest():
    print("going to forest!")
    forest.show_menu()

@beach.command("SHOP")
def enter_shop():
    knife = Weapon("KNIFE", 4)
    knife.set_description("a short, old knife")
    axe = Weapon("AXE", 6)
    axe.set_description("a short and stubby axe")
    tent = Object("TENT")
    tent.set_description("a waterproof tent")

    shop_items = {
        knife: 10,
        axe: 20,
        tent: 25
    }

    shop = Shop("Ethan's Shop", shop_items)
    shop.start_shop(player)
    beach.show_menu()

beach.show_menu()
