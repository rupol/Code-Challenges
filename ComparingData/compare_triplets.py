def compareTriplets(a, b):
    alice_points = 0
    bob_points = 0
    # loop through both arrays
    for i in range(3):
        print(a[i], b[i])
        # compare each item
        # if item a > item b, alice gets a point
        if a[i] > b[i]:
            alice_points += 1
        # if item b > item a, bob gets a point
        elif b[i] > a[i]:
            bob_points += 1
        # if item b = item a, no one gets a point
        # return [alice points, bob points]
    return [alice_points, bob_points]


print(compareTriplets([5, 6, 7], [3, 6, 10]))
