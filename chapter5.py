# chapter5.py
# Function to investigate and collaborate with law enforcement for a raid
def investigate_and_raid():
    print("Armed with proof, you collaborate with the sheriff’s office to raid the society's hideout.")
    action = input("Do you want to proceed with the raid? (y/n): ")
    if action.lower() == 'y':
        return "The raid is a success, but the society’s leader manages to escape."
    else:
        return "You decide to wait for a better opportunity to strike."

# Function to negotiate with the society, risking betrayal
def negotiate_with_society():
    print("You attempt to negotiate with the leader of the secret society.")
    negotiation = input("Do you want to trust the leader and try to reach a compromise? (y/n): ")
    if negotiation.lower() == 'y':
        return "The society leader offers you a deal, but you feel it's too good to be true."
    else:
        return "You decide not to trust them and gather more evidence instead."

# Function to rally the locals to take a stand
def rally_locals():
    print("You gather the townsfolk to stand against the secret society.")
    action = input("Do you want to rally them for a public confrontation? (y/n): ")
    if action.lower() == 'y':
        return "The townspeople gather and confront the society, leading to a dramatic showdown."
    else:
        return "You decide to proceed more cautiously and gather more information before acting."

# Function to review the gathered evidence
def review_evidence():
    print("You review all the clues and evidence you’ve gathered so far.")
    evidence_summary = ["The society has been active for years, with hidden ties to several prominent figures in the town."]
    return evidence_summary