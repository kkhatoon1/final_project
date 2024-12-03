# chapter2.py 
# Function to examine the symbols in the forest
def examine_symbols():
    print("You examine the symbols etched into the trees.")
    symbols = ["The symbols seem to form a pattern, almost like a code."]
    return symbols

# Function to follow the trail deeper into the forest
def follow_trail():
    print("You follow the trail further into the forest.")
    action = input("You start feeling lost. Do you want to keep going? (y/n): ")
    if action.lower() == 'y':
        return "You push forward, but the forest becomes denser."
    else:
        return "You decide to turn back before it gets too dark."

# Function to make camp for the night and review clues
def make_camp():
    print("You set up camp for the night. It's quiet, but something feels wrong.")
    clues = ["You go over your notes and start seeing patterns emerging."]
    return clues

# Function to return to the town for more information
def return_to_town():
    print("You decide to head back to Eldridge for more information.")
    return "Returning to Eldridge."
