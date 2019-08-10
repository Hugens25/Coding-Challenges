# Objective of code is to find most frequent integer in an array

import random

#generate random list
random_list = []
for i in range(50):
    random_list.append(random.randint(1,51))

# num_counts dictionary will keep track of numbers and how many occurances they
# have in the list. ie: {number: occurances}
num_counts = {}

# max_count will keep track of the maximum occurances in the list.
max_count = 0

for val in random_list:
    # check to see if we can add one to the current value without an error.
    # if there is an error in this operation, that means the num_counts dictionary
    # does not contain the key we are trying to manipulate. If there is NO error
    # performing this operation, that means the current number exists as a key
    # in our dictionary, so we can go ahead and increment the value to the key.
    try:
        num_counts[val] += 1
        if num_counts[val] > max_count:
            max_count = num_counts[val]
    except:
        num_counts[val] = 1

# go through the list to report ALL keys who have a value of our max_count. These
# keys contain the most occurances in our list.
for count in num_counts:
    if num_counts[count] == max_count:
        print("{}:{}".format(count, num_counts[count]))

# print functions to print out the max_count and the list of values for checking.
print("max_count is: {}".format(max_count))
print(num_counts)
