# Objective of this solution is to find pairs of integers in a list that
# equal 10. Bonus is to solve problem in linear time.

import random

# this list will store random values for our function
random_list = []

# seed the list with random values from 1 to 9
for i in range(10):
    random_list.append(random.randint(1,9))

# nums_needed will store the values needed in the random_list in order for a
# pair to be found which equals 10.
nums_needed = []

# sums will store all of our pairs which have a sum of 10
sums = []

# print statement to check the values stored in the random_list
print("\nrandom_list: {}".format(random_list))

# for every value in our random list, we must find the complimentary value
# which would give us a sum of 10. Store these complimentary values in nums_needed.
for val in random_list:
    nums_needed.append(10 - val)

# for each complimentary value in nums_needed, check if that value exists in our
# random_list. If it does, we found a matching pair, so we must append that pair
# to our sums list AND remove both values of the pair from our random_list to prevent
# duplicate pairing.
for check_val in nums_needed:
    if check_val in random_list and (10 - check_val) in random_list:
        sums.append((10 - check_val, check_val))

        # This is an ugly work-around for the case where we have ONE 5 in our random_list
        # and ONE 5 in our nums_needed list. Without this workaround, we get a ValueError
        # because we remove 5 from the random_list, then we try to remove 10 - 5 (which is 5) from the
        # random_list again, which results in an error, because we deleted the only 5 which existed
        # in the list. If we encounter this error, that means we already appended (5,5) as a pair to
        # our sums list, so we should remove that faulty pair from our list.
        try:
            random_list.remove(check_val)
            random_list.remove(10 - check_val)
        except:
            sums.remove((10 - check_val, check_val))


print("Sums that equal 10: {}\n".format(sums))
