"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    inv = {}
    for item in items:
        inv[item] = inv.get(item, 0) + 1
    return inv

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    tmp = create_inventory(items)
    for key, value in tmp.items():
        inventory[key] = inventory.get(key, 0) + value
    return inventory

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    tmp = create_inventory(items)
    for key, value in tmp.items():
        tmpval = inventory.get(key,-1)
        if tmpval == -1:
            continue
        if tmpval - value < 0:
            inventory[key] = 0
        else:
            inventory[key] = tmpval - value
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    inventory.pop(item, inventory)
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    inv_list = []
    for key, value in inventory.items():
        if value > 0:
            inv_list.append((key, value))
        
    return inv_list