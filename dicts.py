
def create_inventory(items):
    inventory = {}
    for item in items:
        if item not in inventory:
            inventory[item] = 0
        inventory[item] += 1
    return inventory

def add_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory
    


def decrement_items(inventory, items):
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventory

def list_inventory(inventory):
    inventory_list = []
    for item, count in inventory.items():
        if count > 0:
            inventory_list.append((item, count))
    return inventory_list

