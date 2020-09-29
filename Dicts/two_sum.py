# input: array of integers and target integer
# output: indices of the two numbers in the array that add up to target
# each array will have one solution
# can't use the same element twice

def twoSum(nums, target):
    # create dict to store
    # key: target - num
    # value: index of the num
    num_dict = {(target - num): index for (index, num) in enumerate(nums)}

    # iterate through nums
    for index, num in enumerate(nums):
        # search for num in the dict, if it exists, this is the pair
        if num_dict.get(num):
            if index != num_dict[num]:
                result = [index, num_dict[num]]

    # return the indices of the two nums
    return result


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # expected: [0,1] -> 2 + 7 = 9
