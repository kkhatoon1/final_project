#chapter4.py
# Function to enter the secret society’s hidden lair
def enter_hidden_lair():
    print("You find a hidden door beneath an old abandoned structure. It's time to enter.")
    action = input("Do you want to enter the secret lair? (y/n): ")
    if action.lower() == 'y':
        return "You sneak inside and begin to search for evidence."
    else:
        return "You decide to leave for now, but the society is watching."

# Function to confront the leader of the society
def confront_society_leader():
    print("You come face-to-face with the leader of the secret society.")
    confrontation = input("Do you want to confront the leader directly? (y/n): ")
    if confrontation.lower() == 'y':
        return "The leader becomes defensive and starts to threaten you."
    else:
        return "You decide to gather more evidence before confronting the leader."

# Function to search for information about the missing people
def search_for_missing_people_info():
    print("You look through hidden documents and files in the lair.")
    clues = ["There are records of the missing people, but the documents are coded and hard to understand."]
    return clues

# Function to request backup (may result in the society getting alerted)
def request_backup():
    print("You consider calling for backup. However, it might tip off the society.")
    decision = input("Do you want to call for backup? (y/n): ")
    if decision.lower() == 'y':
        return "Backup is on the way, but you fear the society will notice."
    else:
        return "You choose to stay low for now and continue gathering evidence."