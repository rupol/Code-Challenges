'''
Cookie Monster can eat either 1, 2, or 3 cookies at a time. If he were given a jar of cookies with `n` cookies inside of it, how many ways could he eat all `n` cookies in the cookie jar? Implement a function `eating_cookies` that counts the number of possible ways Cookie Monster can eat all of the cookies in the jar.

For example, for a jar of cookies with `n = 3` (the jar has 3 cookies inside it), there are 4 possible ways for Cookie Monster to eat all the cookies inside it:

1.  He can eat 1 cookie at a time 3 times
2.  He can eat 1 cookie, then 2 cookies
3.  He can eat 2 cookies, then 1 cookie
4.  He can eat 3 cookies all at once.

Thus, `eating_cookies(3)` should return an answer of 4.

Input: an integer
Returns: an integer
'''
import functools


# return the number of ways n cookies can be eaten if cookies can be eaten one, two, or three at a time
# memoization
def eating_cookies(n, cache={}):
    # base cases
    # only once you reach zero cookies do you know you've found 1 way of eating cookies
    if n == 0:
        cache[1] = 1
        return 1
    # if you reach a negative number, you've eaten too many cookies, and have not found a way to eat the correct number of cookies
    if n < 0:
        cache[0] = 0
        return 0

    if n in cache:
        return cache[n]

    # recursive case
    # eating 3 cookies, eating 2 cookies, eating 1 cookie
    result = eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)
    cache[n] = result
    return result


'''
# memoization
@functools.lru_cache()

# first pass solution
# runtime complexity O(3^n) - at any moment, we have one of three options to go down
def eating_cookies(n):
    # base cases
    # 0 ways to eat negative cookies
    if n < 0:
        return 0
    # 1 way to eat 0 cookies
    if n == 0:
        return 1
    # recursive case
    # eating 3 cookies, eating 2 cookies, eating 1 cookie
    return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)
'''

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
