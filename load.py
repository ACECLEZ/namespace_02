import json

# ====== Create weapon data ======
weapon_data = {
    'wooden_sword': {
        'name':'Wooden sword',
        'item_id': 1,
        'stock_available': 20,
        'selling_price': 5.0
    },
    'iron_sword': {
        'name':'Iron sword',
        'item_id': 2,
        'stock_available': 10,
        'selling_price': 10.0
    },
    'diamond_sword': {
        'name':'Diamond sword',
        'item_id': 3,
        'stock_available': 5,
        'selling_price': 30.0
    }
}

# Store this in a JSON file
with open("weapon.json", "w") as f:
    json.dump(weapon_data, f)

# ====== Create armour data ======
armour_data = {
    'iron_helmet': {
        'name':'Iron helmet',
        'item_id': 101,
        'stock_available': 5,
        'selling_price': 12.0
    },
    'iron_chestplate': {
        'name':'Iron chestplate',
        'item_id': 102,
        'stock_available': 3,
        'selling_price': 15.0
    }
}

with open("armour.json", "w") as f:
    json.dump(armour_data, f)