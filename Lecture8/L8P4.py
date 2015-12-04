def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in xrange(2**N):
        combo = []
        for j in xrange(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

# pleh = powerSet([1, 2, 3])
# for i in range(8):
#     print(pleh.next())


def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as
      a list of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in xrange(3**N):
        bag1 = []
        bag2 = []
        for j in xrange(N):
            # test bit jth of integer: if 0, not in either bag; if 1, is in bag1; if 2, is in bag2
            # recall that '>>' is binary shifting! need to consider numbers as ternary, and therefore shift by 3 j times
            # (i.e. divide by 3**j)
            if (i / 3**j) % 3 == 1:
                bag1.append(items[j])
            elif (i / 3**j) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)

pleh = yieldAllCombos([1, 2, 3])
for i in range(27):
    print(pleh.next())

# for i in xrange(2**3):
#     for j in xrange(3):
#         print((i>>j) % 3)
#     print('\n')