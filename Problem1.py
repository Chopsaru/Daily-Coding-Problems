#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#Bonus: Can you do this in one pass?

numlist = [10, 15, 3, 8]
numsum = 18


def checksum(listin, k):
    for i, e in enumerate(listin):
        # if we are at the last int in the list, ad the first int
        if i == len(listin)-1:
            if e + listin[0] == k:
                return True
        else:
            if e + listin[i+1] == k:
                return True
    return False


print(checksum(numlist, numsum))