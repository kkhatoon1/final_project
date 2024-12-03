#khateeja khatoon
# chapter 1 
 
# Function to engage with the sheriff
def engage_with_sheriff():
    print("You meet the local sheriff. He is cautious and unwilling to share much.")
    clues = ["Sheriff mentions missing people in the nearby forest."]
    return clues

# Function to talk to locals at the café
def talk_to_locals():
    print("You talk to the locals at the café. They seem uneasy.")
    rumors = ["Some people say strange figures have been seen near the forest at night."]
    return rumors

# Function to explore the plaza
def explore_plaza():
    print("The village plaza seems peaceful, but something feels off.")
    clues = ["A strange symbol is carved into the fountain."]
    return clues

# Function to investigate the forest (leading to Chapter 2)
def investigate_forest():
    print("You decide to venture into the forest, hoping to find some clues.")
    action = input("Do you want to proceed to the forest? (y/n): ")
    if action.lower() == 'y':
        return "Moving to the forest for investigation."
    else:
        return "You decide to gather more information before venturing into the woods."
