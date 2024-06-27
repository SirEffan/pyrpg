from lib.environment import Environment
from lib.character import Player
player = Player("Vex")



beach = Environment("Beachy Forest")
beach.set_text("You've got to a beach and you see trees in the horizon.")

forest = Environment("Forest")
forest.set_text("you're at the forest!")

@beach.command("Go To Forest")
def gotoforest():
    print("going to forest!")
    forest.show_menu()

beach.show_menu()