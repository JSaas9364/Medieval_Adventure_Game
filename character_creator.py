import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# Load race data
def load_race_data():
    with open("races.json", "r") as file:
        return json.load(file)

race_data = load_race_data()

# Main Window
window = tk.Tk()
window.title("Character Creator")
window.geometry("1200x800")

# Configure grid layout
window.grid_columnconfigure(0, weight=7)  # 70% for stats/perks
window.grid_columnconfigure(1, weight=3)  # 30% for selection
window.grid_rowconfigure(0, weight=1)

# === LEFT SIDE ===
left_frame = tk.Frame(window, bg="lightblue")
left_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

# === RIGHT SIDE ===
right_frame = tk.Frame(window, bg="lightgray")
right_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

# --- LEFT CONTENT ---
stats_label = tk.Label(left_frame, text="Character Stats", font=("Helvetica", 20), bg="lightblue")
stats_label.pack(pady=10)

stats_text = tk.Text(left_frame, height=10, width=60, wrap="word", font=("Helvetica", 14))
stats_text.insert(tk.END, "Select a race to view stats...\n")
stats_text.pack(pady=10)

perks_label = tk.Label(left_frame, text="Racial Perks", font=("Helvetica", 20), bg="lightblue")
perks_label.pack(pady=10)

perks_text = tk.Text(left_frame, height=15, width=60, wrap="word", font=("Helvetica", 14))
perks_text.insert(tk.END, "Select a race to view perks...\n")
perks_text.pack(pady=10)

# --- RIGHT CONTENT ---
select_label = tk.Label(right_frame, text="Select Your Race", font=("Helvetica", 18), bg="lightgray")
select_label.pack(pady=(10, 5))

race_var = tk.StringVar(window)
race_var.set("Human")

race_menu = tk.OptionMenu(right_frame, race_var, *race_data.keys())
race_menu.config(width=20, font=("Helvetica", 14))
race_menu.pack(pady=10)

select_button = tk.Button(right_frame, text="Select Race", command=lambda: update_character_display(race_var.get()), width=20, font=("Helvetica", 14))
select_button.pack(pady=10)

name_label = tk.Label(right_frame, text="Enter Character Name:", font=("Helvetica", 16), bg="lightgray")
name_label.pack(pady=20)

name_entry = tk.Entry(right_frame, font=("Helvetica", 14), width=25)
name_entry.pack(pady=5)


'''
SAVE YOUR CHARACTER CODE START
'''
# --- Save + Confirmation ---
def confirm_and_save_character():
    name = name_entry.get().strip()
    race = race_var.get().strip()

    if not name:
        messagebox.showerror("Missing Name", "Please enter a character name.")
        return

    if race not in race_data:
        messagebox.showerror("Invalid Race", "Please select a valid race.")
        return

    confirm = messagebox.askyesno("Are You Ready?", f"Begin your adventure as {name} the {race}?")
    if not confirm:
        return

    save_character(name, race)


def save_character(name, race):
    data = race_data[race]

    character = {
        "name": name,
        "race": race,
        "level": 1,  # default starting level
        "stats": data.get("stat_modifiers", {}),
        "racial_perks": data.get("racial_perks", {}),
        "magic_restrictions": data.get("magic_restrictions", {}),
        "legendary_perk": data.get("legendary_perk", {}),
        "heroics": data.get("heroics", {}),
        "armor_effects": data.get("armor_effects", {})
    }

    os.makedirs("characters", exist_ok=True)
    filepath = os.path.join("characters", f"{name}_{race}.json")

    with open(filepath, "w") as file:
        json.dump(character, file, indent=4)

    messagebox.showinfo("Character Saved", f"{name} the {race} has begun their journey!")

create_button = tk.Button(
    right_frame,
    text="Create Character",
    width=20,
    font=("Helvetica", 14),
    command=confirm_and_save_character
)
create_button.pack(pady=20)

'''
SAVE YOUR CHARACTER CODE END
'''


# --- Function to update left panel ---
def update_character_display(race):
    race_info = race_data[race]
    stats = race_info["stat_modifiers"]
    perks = race_info["racial_perks"]

    stats_text.delete(1.0, tk.END)

    base_value = 10  # Default base stat for all

    for stat, modifier_str in stats.items():
        percent = int(modifier_str)
        final_value = base_value + int(base_value * percent / 100)
        sign = "+" if percent >= 0 else ""
        stats_text.insert(tk.END, f"{stat}: {final_value} ({sign}{percent}%)\n")


    perks_text.delete(1.0, tk.END)
    for name, desc in perks.items():
        perks_text.insert(tk.END, f"{name} – {desc}\n\n")

# Run the app
window.mainloop()


