#maingame.py
import chapter1
import chapter2
import chapter3
import chapter4
import chapter5

def start_game():
    print("Welcome to the Mystery Game! The town of Eldridge awaits you.")
    input("Press Enter to begin...")
    
    # Chapter 1 - Initial Investigation
    clues = chapter1.engage_with_sheriff()
    print(clues)
    rumors = chapter1.talk_to_locals()
    print(rumors)
    plaza_clues = chapter1.explore_plaza()
    print(plaza_clues)
    
    action = chapter1.investigate_forest()
    print(action)

    # Chapter 2 - Into the Woods
    symbols = chapter2.examine_symbols()
    print(symbols)
    trail_action = chapter2.follow_trail()
    print(trail_action)
    camp_clues = chapter2.make_camp()
    print(camp_clues)
    return_to_town = chapter2.return_to_town()
    print(return_to_town)

    # Chapter 3 - The Web Unravels
    suspects = ["Sheriff", "Local shopkeeper"]
    interrogation = chapter3.interrogate_suspects(suspects)
    print(interrogation)
    town_conflict = chapter3.attend_town_meeting()
    print(town_conflict)
    library_info = chapter3.visit_town_library()
    print(library_info)
    individual_tracking = chapter3.track_down_individuals()
    print(individual_tracking)

    # Chapter 4 - Hidden Lair
    lair_action = chapter4.enter_hidden_lair()
    print(lair_action)
    society_confrontation = chapter4.confront_society_leader()
    print(society_confrontation)
    missing_people_info = chapter4.search_for_missing_people_info()
    print(missing_people_info)
    backup_request = chapter4.request_backup()
    print(backup_request)

    # Chapter 5 - Final Confrontation
    raid_action = chapter5.investigate_and_raid()
    print(raid_action)
    negotiation_action = chapter5.negotiate_with_society()
    print(negotiation_action)
    rally_action = chapter5.rally_locals()
    print(rally_action)
    review_clues = chapter5.review_evidence()
    print(review_clues)

    print("Game Over. The mystery of Eldridge has been solved.")

# Start the game
start_game()