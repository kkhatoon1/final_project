#chapter3.py
def interrogate_suspects(suspects):
    print("You decide to interrogate the suspects you’ve met so far.")
    for suspect in suspects:
        print(f"Interrogating {suspect}:")
        if suspect == "Sheriff":
            print("The sheriff seems nervous and doesn’t provide much detail.")
        elif suspect == "Local shopkeeper":
            print("The shopkeeper offers some useful insights, but is clearly hiding something.")
        else:
            print(f"{suspect} seems to know more than they're letting on.")
    return "Interrogation completed."

# Function to attend a town meeting and observe relationships between locals
def attend_town_meeting():
    print("You attend the town meeting. People are discussing recent events.")
    town_conflict = ["There's a lot of tension about the missing people. Some blame the sheriff, others are suspicious of outsiders."]
    return town_conflict

# Function to visit the town library and look up the town's history
def visit_town_library():
    print("You head to the local library to research Eldridge’s history.")
    history = ["Eldridge has a dark past, with rumors of secret societies and unexplained events dating back decades."]
    return history

# Function to track down dubious individuals based on clues
def track_down_individuals():
    print("You decide to follow a suspicious individual who has been acting strangely.")
    action = input("Do you want to follow the person covertly? (y/n): ")
    if action.lower() == 'y':
        return "You follow the individual and find them meeting with a mysterious figure."
    else:
        return "You lose track of the person, but the suspicion remains."