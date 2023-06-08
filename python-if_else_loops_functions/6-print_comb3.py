#!/usr/bin/python3
# outer loops, iterates through the first set of numbers.
for i in range(0, 10):
    # inner loop, iterates through the second set of numbers.
    # begins at the value i+1, at no point will i==j
    for j in range(i+1, 10):
        # checks if i = 8 and j= 9, the largest possible values for both
        # if true, we've got the largest value. the sep="" indicates no
        # separation between the numbers.
        if i == 8 and j == 9:
            print("{}{}".format(i, j), sep="")
        else:
            print("{}{}".format(i, j), sep="", end=" ,")
