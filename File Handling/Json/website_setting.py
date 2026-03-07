import json
import os

# We don't necessarily need a global listdata if we load from the file
filename = "config.json"

def website():
    # New data to be added
    data = {
        "title": "Food Plaza", 
        "theme": "Italic",
        "font_size": 48
    }
    
    if os.path.exists(filename):
        # 1. Read the existing data first
        with open(filename, "r") as file:
            # Load current list from file
            listdata = json.load(file)
        
        # 2. Add the new dictionary to that list
        listdata.append(data)
        
        # 3. Save the combined list back to the file
        with open(filename, "w") as file:
            json.dump(listdata, file, indent=4)
            
        print(f"Data successfully added to {filename}.")
    else:
        print(f"Error: {filename} does not exist. Please create it first.")

# Run the function
website()


def update_grocery_list():
    # The new items we want to add
    new_items = ["Cereal", "Orange Juice", "Butter"]
    
    filename = "grocery.json"

    # 1. Check if the file exists so we don't get an error
    if os.path.exists(filename):
        # 2. Open and read the current list
        with open(filename, "r") as file:
            current_data = json.load(file)
            
        # 3. Combine the existing list with the new items
        # If the file was just a list of strings, we use .extend()
        current_data.extend(new_items)
        
        # 4. Save the updated list back to the same file
        with open(filename, "w") as file:
            json.dump(current_data, file, indent=4)
        
        print(f"Successfully updated {filename} with {len(new_items)} new items.")
    else:
        print(f"Error: {filename} does not exist. Please create it first.")

# Run the update
update_grocery_list()