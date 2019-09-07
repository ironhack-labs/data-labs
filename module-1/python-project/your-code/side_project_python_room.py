# DEPENDENCIES

# NAMING CONVENTIONS
# doors have a lowercase letter
# keys have a lowercase letter matching the door they unlock
# rooms have a number

'''
Possible Improvements
---------------------
1. display current location at the top and current inventory (collected keys)
2. import os, os.system("clear") to get rid of the long lines in the terminal (do this last, will make it more difficult to debug) (throw that right into the startGame function for immersion)
startGame = press enter to start, wait for input() with no argument

3. add a call for help
4. organize the furniture, doors, and keys together for defining (make it easier to add new rooms and objects)

# define rooms and items (organized by which room they are found in)

couch = {
    "name": "couch",
    "type": "furniture",
}

door_a = {
    "name": "door a",
    "type": "door",
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

piano = {
    "name": "piano",
    "type": "furniture",
}

game_room = {
    "name": "game room",
    "type": "room",
}

bedroom1 = {
    "name": "bedroom 1",
    "type": "room",
}

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
}


door_b = {
    "name": "door b",
    "type": "door",
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

door_c = {
    "name": "door c",
    "type": "door",
}

bedroom2 = {
    "name": "bedroom 2",
    "type": "room",
}

double_bed = {
    "name": "double bed",
    "type": "furniture",
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}

dresser = {
    "name": "dresser",
    "type": "furniture"
}

door_d = {
    "name": "door d",
    "type": "door",
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}

living_room = {
    "name": "living room",
    "type": "room",
}

dining_table = {
    "name": "dining table",
    "type": "furniture"
}


outside = {
  "name": "outside"
}

all_rooms = [
    game_room, 
    bedroom1, 
    bedroom2,
    living_room, 
    outside
]

all_doors = [
    door_a, 
    door_b, 
    door_c,
    door_d,
]

# define which items/rooms are related

object_relations = {
    "outside": [door_d],
    "game room": [couch, piano, door_a],
    "piano": [key_a],
    "door a": [game_room, bedroom1],
    "bedroom 1": [queen_bed, door_a, door_b, door_c],
    "queen bed": [key_b],
    "door b": [bedroom1, bedroom2], # temporarily assign this to outside, don't forget to come back and fix!
    "bedroom 2": [double_bed, dresser, door_b], # whats in this room?
    "double bed": [key_c],
    "dresser": [key_d],
    "door c": [bedroom1, living_room],
    "living room": [dining_table, door_c, door_d],
    "door d": [living_room, outside]
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}

def lineBreak():
    print("\n\n")

def startGame(): # initialize the game
    print("You wake up on a couch and find yourself in a strange house with no windows which you have never been to before. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!")
    playRoom(game_state["current_room"])

def playRoom(room, optional_msg = None): # look at DJK's code for the "if optional_msg: print(optional_msg)"
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        print("Congrats! You escaped the room!")
    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type 'explore' or 'examine'?").strip()
        if intended_action == "explore":
            exploreRoom(room)
            playRoom(room)
        elif intended_action == "examine":
            examineItem(input("What would you like to examine?").strip())
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'.")
            playRoom(room)
        lineBreak()

def exploreRoom(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))

def getNextConnectedRoom(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room

def examineItem(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been 
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None
    
    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = "You examine " + item_name + ". "
            if(item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    output += "You unlock it with a key you have."
                    next_room = getNextConnectedRoom(item, current_room)
                else:
                    output += "It is locked but you don't have the key."
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                else:
                    output += "There isn't anything interesting about it."
            print(output)
            break

    if(output is None):
        print("The item you requested is not found in the current room.")
    
    if(next_room and input("Do you want to go to the next room? Enter 'yes' or 'no'").strip() == 'yes'):
        playRoom(next_room)
    else:
        playRoom(current_room)

game_state = INIT_GAME_STATE.copy()

startGame()