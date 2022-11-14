def recursive(x):
    print(x)
    if x == 0:
        print('if')
        return x
    else:
        print('else')
        recursive(x-1)


def recursiveNew(x):
    print(x)
    if x == 0:
        return 10
    return x + recursiveNew(x-1)


print(recursiveNew(5))



# let's do the easy way first, track the Sum total in an extra parameter
# this is similar to your homework sample
'''
def sumRecursive1(x, total):
    print("value x=", x, " and total tracking = ", total)
    if x == 0:
        return total
    total+=x
    return sumRecursive1(x-1, total)


def sumRecursive2(x, total):
    print("value x=", x, " 2 and total tracking = ", total)
    if x == 0:
        return total

    return sumRecursive2(x-1, total+x)


print(sumRecursive2(5, 0))
'''