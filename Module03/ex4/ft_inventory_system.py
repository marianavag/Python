import sys


def get_inventory() -> dict:
    """Build inventory dictionary from command-line arguments."""
    items = sys.argv[1:]
    inventory = {}
    for item in items:
        name = ""
        qty_str = ""
        found_colon = False
        for char in item:
            if char == ":" and not found_colon:
                found_colon = True
            elif not found_colon:
                name += char
            else:
                qty_str += char
        qty = int(qty_str)
        inventory[name] = {"quantity": qty}
    return inventory


def sort_inventory(inventory: dict) -> dict:
    """Return inventory sorted by qty (descending)."""
    temp = dict(inventory)
    sorted_inventory = {}
    while len(temp) > 0:
        max_name = ""
        max_qty = -1
        for name, data in temp.items():
            qty = data["quantity"]
            if qty > max_qty:
                max_qty = qty
                max_name = name
        sorted_inventory.update({max_name: temp[max_name]})
        del temp[max_name]
    return sorted_inventory


def ft_inventory_system(original: dict, sorted_inv: dict) -> None:
    """Print inventory analysis, statistics, and management suggestions
    and keeps the original input for more data statistics."""
    if not sorted_inv:
        print("Inventory is empty")
        return
    if not original:
        print("Inventory is empty")
        return
    print("=== Inventory System Analysis ===")
    total_items = 0
    for data in sorted_inv.values():
        total_items += data["quantity"]
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(sorted_inv)}")
    print("\n=== Current Inventory ===")
    for name, data in sorted_inv.items():
        qty = data["quantity"]
        percentage = (qty/total_items) * 100
        if qty > 1:
            print(f"{name}: {qty} units ({percentage:.1f}%)")
        else:
            print(f"{name}: {qty} unit ({percentage:.1f}%)")
    print("\n=== Inventory Statistics ===")
    top_name = ""
    for name in sorted_inv:
        if top_name == "":
            top_name = name
    top_item_qty = sorted_inv[top_name]["quantity"]
    least_name = ""
    min_qty = None
    for name, data in original.items():
        qty = data["quantity"]
        if min_qty is None or qty < min_qty:
            min_qty = qty
            least_name = name
    least_item_qty = min_qty
    print(f"Most abundant: {top_name} ({top_item_qty} units)")
    print(f"Least abundant: {least_name} ({least_item_qty} unit)")
    print("\n=== Item Categories ===")
    moderate = {}
    scarce = {}
    for name, data in original.items():
        qty = data["quantity"]
        if qty >= 5:
            moderate.update({name: qty})
        else:
            scarce.update({name: qty})
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")
    print("\n=== Management Suggestions ===")
    restock = []
    for name, data in sorted_inv.items():
        qty = data["quantity"]
        if qty < 2:
            restock.append(name)
    print(f"Restock needed: {restock}")
    print("\n=== Dictionary Properties Demo ===")
    keys_str = "["
    for name in original.keys():
        keys_str += f"'{name}', "
    keys_str = keys_str[:-2] + "]"
    print(f"Dictionary keys: {keys_str}")
    values_str = "["
    for data in original.values():
        qty = data["quantity"]
        values_str += f"{qty}, "
    values_str = values_str[:-2] + "]"
    print(f"Dictionary values: {values_str}")


if __name__ == "__main__":
    inv_orig = get_inventory()
    inv_sorted = sort_inventory(inv_orig)
    ft_inventory_system(inv_orig, inv_sorted)
    check = inv_orig.get('sword') is not None
    print(f"Sample lookup - 'sword' in inventory: {check}")
