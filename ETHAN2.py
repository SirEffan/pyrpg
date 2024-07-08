# pick weapon: shortsword or knife
# environment (old city?, medieval?)
# shop (in city)
# merchant in shop (NPC)
# Talk to merchant
# choice:
#   - get mad
#   - you buy stuff
# if he gets mad, then start combat

from lib.character import Character, Player
from lib.container import Weapon
from lib.environment import Environment
from lib.templates.combat import Combat
from lib.templates.shop import Shop

oldcity = Environment("Old City")
oldcity.text = "You're in an old city and you see a merchant.\nDo you want to talk to him?"

shortsword = Weapon("Short Sword", 6)
knife = Weapon("Knife", 6)
longbow = Weapon("Long Bow", 20)
greatsword = Weapon("Great Sword", 20)

player = Player("Andir")
player.gold = 5
elderix = Character("Elderix", greatsword)

shop_items = {
    longbow: 250,
    greatsword: 200,
}
shop = Shop("Elderix's Shop", player, shop_items)

@oldcity.command("Talk to merchant")
def f():
    talk_to_elderix = Environment("Talk to Elderix")
    talk_to_elderix.text = """Hello, traveler! I am Elderix, the shopkeeper.
You seem rich! I will make you pay a lot of money for the stuff in my shop"""

    @talk_to_elderix.command("Hey, that's not fair! I will fight you")
    def fight():
        combat_scene = Combat(player, elderix)
        combat_scene.initiate_combat()

    @talk_to_elderix.command("Hey, that's not fair! I will return to the city")
    def return_to_city():
        oldcity.show_menu()

    @talk_to_elderix.command("Okay, I will enter the shop")
    def enter_shop():
        shop.start_shop()
    
    talk_to_elderix.show_menu()

choose_weapon = Environment("Weapon")
choose_weapon.text = "Choose your weapon!"

@choose_weapon.command("A Short Sword")
def shs():
    print("You chose the Short Sword!")
    player.give_item(shortsword)


@choose_weapon.command("A Knife")
def kn():
    print("You chose the Knife!")
    player.give_item(knife)

choose_weapon.show_menu()
oldcity.show_menu()
