# python2
'''
binarySearch.py
input: a sorted list (arr) and a value to search for (x)
output: the index in A for each element of B; -1 if value not found in A
'''
import sys

def binarySearch(arr, left, right, x):
    #left, right = 0, len(arr)
    midpoint = left + (right - left)//2
    #print 'midpoint: ' + str(midpoint)
    
    if x == arr[midpoint]:
        #print 'Found at midpoint! Array: ' + str(arr) + ' midpoint: ' + str(midpoint)
        return midpoint
    
    if right - left == 1:
        #print str(x) + ' not found!'
        return -1
        
    if x < arr[midpoint]:
        #print 'Search left of ' + str(arr[midpoint]) + ' left: ' + str(left) + ' right: ' + str(midpoint)
        return binarySearch(arr, left, midpoint, x)
    
    #print 'Search right of ' + str(arr[midpoint]) + ' left: ' + str(midpoint) + ' right: ' + str(right)
    return binarySearch(arr, midpoint, right, x)
    #if rightIndex == -1:
     #   return rightIndex
    #return midpoint + rightIndex

# TEST CASES
'''
a = [1,5,8,12,13]
print binarySearch(a, 0, len(a), 8) #expect 2
print binarySearch(a, 0, len(a), 1) #expect 0
print binarySearch(a, 0, len(a), 23) #expect -1
print binarySearch(a, 0, len(a), 1) #expect 0
print binarySearch(a, 0, len(a), 11) #expect -1
print binarySearch(a, 0, len(a), 12) #expect 3
print binarySearch(a, 0, len(a), -1) #expect -1
#'''


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

#'''
# Reads from stdin for assignment
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print binarySearch(a, 0, len(a), x),
#'''