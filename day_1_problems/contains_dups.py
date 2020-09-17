# input: array of ints
# output: true/false
# true: there are duplicates in input array
# false: no dups

def containsDuplicate(nums):
    # create set to store already seen values
    seen = set()
    # iterate through array
    for int in nums:
        # add elements as we come across new ones
        if int not in seen:
            seen.add(int)
        # return true if element is already in seen (it's a dup)
        else:
            return True
    return False


print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
print(containsDuplicate([1, 2, 3, 4]))
