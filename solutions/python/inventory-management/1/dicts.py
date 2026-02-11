"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    count = 0
    inventory = {}
    new = []
    for item in items:
        count = 0
        if item in inventory:
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1
            # continue
        # count=items.count(item)
        # print(item,count)
        # dictionary = dictionary 
        # print('debug')
        # print(dictionary)
    return inventory

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for item in items:
        if item in inventory:
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1
    return inventory

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for item in items:
        if item not in inventory:
            continue
        #     inventory[item] = 1
        #     print('debug',item)
        if inventory[item] == 0:
            continue
        if item in inventory:
            inventory[item] = inventory[item] - 1
            print(inventory[item],item)
        # if item not in inventory:
        #     inventory[item] = 1
        #     print('debug',item)
            
        # else:
        #     inventory[item] = 0
        #     print[inventory[item],item]
    # print(inventory)
    return inventory

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory:
        inventory.pop(item)
    return inventory

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    # """
    # if inventory.values() == 0:
    #     print('debug')
    #     pass
    # else:
    #     list_of_items = list(inventory.items())
    #     list_of_items.pop
    #     return list_of_items
    list_of_items = []
    for keys,values in inventory.items():
        if values != 0:
            list_of_items.append((keys,values))
    return list_of_items