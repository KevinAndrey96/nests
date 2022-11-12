"""
Write a function occupy(n), which shows how birds are going to occupy n nests, assuming
that each new bird will choose the nest in the middle of the largest unoccupied run of nests.
You could use as a helper function longestFalse(L) from the previous question. For example,
if there were 10 nests, occupy(10) would print out the following sequence, where
underscore indicates an unoccupied nest, and X indicates an occupied nest. The first line of
the printout is just 10 underscores showing that all the nests are unoccupied. The second
line shows that a bird came to nest in position 5, since that is one the first middle positions
of the unoccupied run from 0 to 9. In the third line a bird came to occupy the middle
position for the longest open run of nests, from 0 to index 4.

_ _ _ _ _ _ _ _ _ _
_ _ _ _ _ X _ _ _ _
_ _ X _ _ X _ _ _ _
_ _ X _ _ X _ _ X _
and so on, until
X X X X X X X X X X

"""

import math

def longestFalse(l):
    maxStart = 0
    maxEnd = len(L)

    start = 0
    end = len(L)

    startFounded = False
    endFounded = False

    longitude = 0

    # check starting index
    for i in range(0, len(l)):
        if startFounded == False and l[i] == False:
            start = i
            startFounded = True
            continue
        if startFounded == True and (l[i] == True or i == len(l) - 1):
            end = i
            endFounded = True

        if startFounded == True and endFounded == True:
            newLongitude = end - start
            if newLongitude >= longitude:
                longitude = newLongitude
                maxStart = start
                maxEnd = end
            startFounded = False
            endFounded = False

    return maxStart, maxEnd

def formatList(l):
    formattedList = ''
    for i in range(len(l)):
        if l[i]:
            formattedList += 'x '
            continue
        formattedList += '_ '
    return formattedList

def occupy(l):
    start, end = longestFalse(l)
    index = round((end - start) / 2)
    l[start + index] = True
    return l

if __name__ == '__main__':
    # init vars
    n = 10
    L = [False for i in range(n)]

    for i in range(n):
        L = occupy(L)
        print(formatList(L))
