# 📄 File: inventory_system.py

# Default empty equipment layout
def default_equipment():
    return {
        "weapon": None,
        "offhand": None,
        "head": None,
        "chest": None,
        "legs": None,
        "feet": None,
        "ring_1": None,
        "ring_2": None,
        "amulet": None,
        "relic": None
    }

# Default empty inventory
def default_inventory():
    return []

# Example equip function (stub)
def equip_item(equipment, inventory, item, slot):
    if slot not in equipment:
        raise ValueError(f"Invalid slot: {slot}")

    # If something is already equipped in the selected slot, unequip it first
    if equipment[slot] is not None:
        inventory.append(equipment[slot])

    equipment[slot] = item
    if item in inventory:
        inventory.remove(item)

# Example unequip function (stub)
def unequip_item(equipment, inventory, slot):
    item = equipment.get(slot)
    if item:
        inventory.append(item)
        equipment[slot] = None
