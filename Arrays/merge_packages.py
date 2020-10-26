# input: array of integers, limit
# output: first two elements whose sum equals limit, ordered small to large

def merge_packages(items, limit):
    # create dict to store
    # key: limit - item
    # value: index of the item
    item_dict = {(limit - item): index for (index, item) in enumerate(items)}
    item_indices = []
    # iterate through items
    for index, item in enumerate(items):
        # search for item in the dict, if it exists, this is the pair
        if item in item_dict:
            if index != item_dict[item]:
                # order item indices from large to small
                if index < item_dict[item]:
                    item_indices = [item_dict[item], index]
                else:
                    item_indices = [index, item_dict[item]]

    return item_indices

# One pass solution


def merge_packages_opt(items, limit):
    cache = {}
    item_indices = []
    for index, item in enumerate(items):
        possible_match = cache.get(limit - item)
        if possible_match is not None and possible_match != index:
            # order item indices from large to small
            if index < possible_match:
                item_indices = [possible_match, index]
            else:
                item_indices = [index, possible_match]
        cache[item] = index
    return item_indices


print(merge_packages([4, 6, 10, 15, 16], 21))
print(merge_packages_opt([4, 6, 10, 15, 16], 21))
