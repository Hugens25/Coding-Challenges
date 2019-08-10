# The objective of this solution is to compare two lists and see if
# the lists are rotated variations of one another

# this function simply turns a list into a map, storing the list index as the key,
# and the number of occurances of they key in the list as the value. This is used
# later in the code for comparison to the two lists.
def copy_list_to_map(l):
    m = {}
    for value in l:
        try:
            m[value] += 1
        except:
            m[value] = 1
    return m


def main():

    list_one = [2,2,2,5,2,2,2,2]
    list_two = [5,2,2,2,2,2,2,2]

    # boolean to keep track of valid rotated-array orientation(s). Once
    # a rotated-array orientation is found, we report True.
    is_rotated_array = False

    # A base case to see if the two lists are equal in size. If not, we know they
    # cannot be rotated arrays of each other.
    if len(list_one) == len(list_two):
        list_one_map = copy_list_to_map(list_one)
        list_two_map = copy_list_to_map(list_two)

        # Another base case that checks if the two lists contain the same values
        # with the same amount of occurances. Here we convert our lists into maps,
        # and use the map to determine the occurances of each item in the list. If
        # the map values aren't the same, that means the occurances are different,
        # which means our two lists cannot be rotated arrays of one another.
        if list_one_map == list_two_map:

            # We loop through the elements of list one and if we come across a value
            # which equates to the first value stored in list_two, we check to see
            # if we can arrange list_one to equal list_two by splicing list_one from
            # the current index (i) up to it's end element, then appending the first
            # element of list_one up to the ith element. This rearranges list_one in
            # a way that should match up with list_two, if they are rotated arrays of
            # one another.
            for i in range(len(list_one)):
                if list_two[0] == list_one[i]:
                    is_rotated_array = (list_one[i:]+list_one[:i] == list_two)

                    # if this is a valid rotated-array, return true and break,
                    # because we are done.
                    if is_rotated_array:
                        break

    return is_rotated_array

print(main())
