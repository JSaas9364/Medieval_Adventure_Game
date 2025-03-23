import json

# Load races from the races.json file
def load_races():
    with open('races.json', 'r') as f:
        return json.load(f)

# Display the stats and perks for each race
def display_race_details(race, selected_race):
    print(f"\n{selected_race.upper()}")
    print("\nStat Modifiers:")
    for stat, value in race["stat_modifiers"].items():
        print(f"- {stat}: {value}")

    print("\nRacial Perks:")
    for perk, description in race["racial_perks"].items():
        print(f"- {perk}: {description}")

    print("\nArmor Effects:")
    for armor, effect in race["armor_effects"].items():
        print(f"- {armor}: {effect}")

    print("\nLegendary Perk:")
    for perk_name, perk_details in race["legendary_perk"].items():
        print(f"{perk_name}:")
        print(f"  - {perk_details['description']}")
        for bonus, value in perk_details["bonuses"].items():
            print(f"    - {bonus}: {value}")

    print("\nHeroics:")
    for heroics_name, heroics_details in race["heroics"].items():
        print(f"{heroics_name}:")
        for condition, effect in heroics_details.items():
            print(f"  - {condition}: {effect}")

# Character creator function
def character_creator():
    races = load_races()  # Load races data from races.json

    print("Choose your race:")
    for idx, race_name in enumerate(races.keys(), 1):
        print(f"{idx}. {race_name}")

    # Get race selection input
    choice = input("Select race (1-4): ")
    race_keys = list(races.keys())

    try:
        selected_race = race_keys[int(choice) - 1]
    except (ValueError, IndexError):
        print("Invalid choice, please try again.")
        return

    print(f"\nYou selected {selected_race}!")
    display_race_details(races[selected_race], selected_race)

    # Ask the player if they want to continue or change their selection
    continue_creation = input("\nDo you want to continue with this race? (y/n): ").strip().lower()
    if continue_creation == 'y':
        name = input("\nEnter your character's name: ")
        print(f"\nWelcome, {name} the {selected_race}!")
        # Proceed with the game or continue character creation steps...
    elif continue_creation == 'n':
        character_creator()  # Restart the process if the player wants to change race
    else:
        print("Invalid input, please enter 'y' or 'n'.")
        character_creator()  # Prompt again in case of invalid input

if __name__ == "__main__":
    character_creator()
