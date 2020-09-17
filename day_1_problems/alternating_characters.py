# input: string containing A and B (e.g. AABAAB)
# change input into string of alternating As and Bs
# can only delete characters
# output: minimum number of deletions (e.g. AABAAB -> ABAB, 2 deletions)

def alternatingCharacters(s):
    # create counter to track deletions
    deletions = 0
    # iterate through string
    for index, character in enumerate(s[:-1]):
        # if current != next, del next
        print(index, character)
        if character == s[index + 1]:
            deletions += 1
    return deletions


print(alternatingCharacters('AABAAB'))
