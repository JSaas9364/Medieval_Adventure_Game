# Character Races and Stat Blocks

races = {
    "Human": {
        "stat_modifiers": {
            "STR": 0,
            "CON": 0,
            "AGI": 0,
            "INT": 0,
            "WIS": 0
        },
        "racial_perks": {
            "Versatile Learner": "+10% XP gain, +10% reputation gain",
            "Silver Tongue": "-5% reputation loss, +10% charisma with vendors of all races",
            "Hunter-Gatherer": "+10% gathering and hunting speed",
            "Cartographer": "+20% to avoid ambushes, +20% to spot secrets/treasures, extended threat detection",
            "Endurance Runner": "+25% stamina pool",
            "Fading Step": "+10% stealth",
            "Plague-Hardened": "+20% disease resistance",
            "Perfect Guard": "50% chance to riposte (70% reduced damage) if AGI > opponent"
        },
        "armor_effects": {
            "physical_damage_resistance": "+10% with chain or plate armor"
        },
        "legendary_perk": {
            "Cartographer's Legacy": {
                "description": "Immune to ambushes, reveals hidden paths, loot, and threats on the map much more often.",
                "bonuses": {
                    "XP_gain": "+10%",
                    "reputation_gain": "+10%",
                    "travel_action_per_day": "+1 free, ignores stamina cost",
                    "travel_recovery": "Recover stamina and mana while traveling"
                }
            }
        },
        "heroics": {
            "Last Stand": {
                "below_30_hp": "+30% all damage and accuracy, -30% physical/magical damage taken, blocks stop 100% of damage, block chance +25%, +20% max health pool for 10 turns"
            }
        },
        "magic_restrictions": {
            "allowed": ["All"],
            "note": "Humans can use all types of magic without restriction."
        }
    },
    "Elf": {
        "stat_modifiers": {
            "STR": -20,
            "CON": -10,
            "AGI": 20,
            "INT": 0,
            "WIS": 10
        },
        "racial_perks": {
            "Arcane Precision": "+10% max mana and +10% casting speed",
            "Natural Conduit": "+10% mana & stamina regen, +15% in nature",
            "Graceful Striker": "+10% speed with ranged and agility weapons",
            "Fleetfoot": "+10% movement speed",
            "Fading Step": "+10% stealth",
            "Naturebound": "+10% gathering efficiency (wood, herbs, hunting)",
            "Purity of the Grove": "Immunity to lesser poisons and diseases",
            "Kindred Favor": "+10% charisma with Elves, -15% with non-Elves"
        },
        "armor_effects": {
            "plate_armor": "-30% effectiveness",
            "leather_armor": "+10% effectiveness",
            "chain_armor": "+10% effectiveness"
        },
        "legendary_perk": {
            "Eternal Flow": {
                "description": "Passive mana and stamina regeneration increased by 25%.",
                "bonuses": {
                    "mana_cost": "-15% mana cost",
                    "movement_speed": "+15%",
                    "ranged_and_magic_damage": "+10%"
                }
            }
        },
        "heroics": {
            "Sylvan Awakening": {
                "below_50_hp": "+25% movement speed, AGI, casting speed",
                "below_30_hp": "6x health regen in combat (if in nature)",
                "once_per_day": "Escape one battle, recover 30% health, stamina, and mana",
                "if_in_nature": "Regenerate 1% mana and stamina per turn while under 30% HP"
            }
        },
        "magic_restrictions": {
            "allowed": ["Nature"],
            "note": "Can only use Nature magic (includes Fire, Ice, Thunder, and Nature spells)."
        }

    },
    "Orc": {
        "stat_modifiers": {
            "STR": 20,
            "CON": 10,
            "AGI": -20,
            "INT": 0,
            "WIS": -10
        },
        "racial_perks": {
            "Brutal Force": "+10% chance to stagger, -15% accuracy, +15% damage and accuracy vs bleeding enemies, -10% ranged/magic accuracy & casting speed",
            "Hexweaver's Rage": "+20% casting speed for Hexes and Curses",
            "Intimidation Aura": "-10% enemy attack and magic, 10% chance enemies under 20% HP stop attacking",
            "Pack Tactics": "+10% CHA with Orcs, -20% with non-Orcs, +20% intimidation when haggling",
            "Ironhide": "+10% physical, -5% magical resistance, +50% lesser poison, disease, hex, and curse resistance",
            "Savage Endurance": "+10% stamina regen, +15% in combat",
            "Hunter’s Drive": "+20% hunting efficiency",
            "Unrefined Instincts": "-10% stealth, -10% crafting speed"
        },
        "armor_effects": {
            "bone_armor": "+30% effectiveness",
            "leather_armor": "+20% effectiveness",
            "chain_armor": "+10% effectiveness",
            "plate_armor": "-30% effectiveness"
        },
        "legendary_perk": {
            "Wrath Unleashed": {
                "description": "Increases melee damage and accuracy under 50% HP, triggers second wind for stamina regen, and enhances curses/hexes.",
                "bonuses": {
                    "melee_damage": "+30%",
                    "melee_accuracy": "+20%",
                    "curses_and_hexes": "50% stronger, 20% faster",
                    "second_wind": "+20% stamina regen for 10 turns, triggers once every 20 turns"
                }
            }
        },
        "heroics": {
            "Wrath Unleashed": {
                "below_50_hp": "+30% melee damage, +20% melee accuracy",
                "below_30_hp": "+20% chance to stagger on hit, curses and hexes become instant-cast"
            }
        },
        # For Orcs
        "magic_restrictions": {
            "allowed": ["Curses", "Hexes"],
            "note": "Healing magic is 50% less effective unless using curses. Cannot use Holy or Nature magic."
            }
    },
    "Dwarf": {
        "stat_modifiers": {
            "STR": 10,
            "CON": 20,
            "AGI": -20,
            "INT": 0,
            "WIS": -10
        },
        "racial_perks": {
            "Stubborn Will": "Immune to fear and charm",
            "Stonebound Plate": "+10% defense and no movement penalties in full plate",
            "Stoneblood": "+20% physical resistance",
            "Forge Tempered": "+15% fire, ice, lightning resistance",
            "Master Craftsman": "+20% crafting speed, +10% XP in Smithing, Engineering, Mining",
            "Mountain Stamina": "+10% stamina regen, +15% in caves, Nightvision",
            "Battle Trained": "+10% attack and accuracy with axes, hammers, heavy weapons",
            "Steady Hands": "+10% damage blocked with shields"
        },
        "armor_effects": {
            "plate_armor": "+10% armor effectiveness",
            "chain_armor": "+5% effectiveness",
            "leather_armor": "+3% effectiveness"
        },
        "legendary_perk": {
            "Heart of the Mountain": {
                "description": "Increased health regen, immune to stagger, deflect spells with plate armor.",
                "bonuses": {
                    "regen": "2x passive health regeneration",
                    "deflect_spells": "20% chance when wearing plate armor with 75%+ durability"
                }
            }
        },
        "heroics": {
            "Heart of Stone": {
                "below_50_hp": "4x regen",
                "below_30_hp": "6x regen",
                "below_25_hp": "Once per day, regenerate 10% HP per turn until 30%+ HP",
                "if_hp_0": "Once per day, prevent death, remain at 1 HP"
            }
        },
        "magic_restrictions": {
            "allowed": ["Holy"],
            "note": "Can only use Holy magic. Focuses on healing, defense, and buffs. Cannot use Curses, Hexes, Nature, or Elemental magic."
        }

    }
}


import json

with open('races.json', 'w') as f:
    json.dump(races, f, indent=4)
