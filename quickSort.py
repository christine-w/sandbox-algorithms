'''
quickSort.py
input: an array of integers, leftmost index, rightmost index (i.e., len(array) = right - left + 1), (optional) running total of comparisons
output: array is sorted in place, return value is the total number of comparisons made

quick sort has an average running time of O(nlogn)
'''
import random

def quickSort(arr, left, right, numComparisons=[0]):
    #print 'left: ' + str(left) + ' right: ' + str(right) + ' array: ' + str(arr)
    if left >= right:
        #print 'BASE CASE REACHED'
        return numComparisons

    numComparisons[0] += right - left
    '''
    #pivotIndex = left
    #pivotIndex = right
    # median of three pivot choice
    medianIndex = (right - left)//2
    medianValue = sorted([arr[left], arr[left+medianIndex], arr[right]])[1]
    if arr[left] == medianValue:
        pivotIndex = left
    elif arr[left+medianIndex] == medianValue:
        pivotIndex = left + medianIndex
    else:
        pivotIndex = right
    #'''

    pivotIndex = random.randint(left, right)
    partitionIndex = partition(arr, pivotIndex, left, right)
    quickSort(arr, left, partitionIndex - 1, numComparisons)
    quickSort(arr, partitionIndex + 1, right, numComparisons)

    return numComparisons

'''
partition subroutine
input: an array of integers, index of chosen pivot, leftmost index, rightmost index
output: index of pivot after array has been partitioned around the pivot value
'''
def partition(arr, pivotIndex, left, right):
    if pivotIndex != left:
        arr[left], arr[pivotIndex] = arr[pivotIndex], arr[left]
    #print 'pivot: ' + str(arr[left]) + ' pivotIndex: ' + str(pivotIndex) + ' new array: ' + str(arr)

    partitionIndex = left
    for i in range(left + 1, right + 1):
        if arr[i] <= arr[left]:
            partitionIndex += 1
            arr[partitionIndex], arr[i] = arr[i], arr[partitionIndex]
    arr[left], arr[partitionIndex] = arr[partitionIndex], arr[left]
    #print 'partitionIndex: ' + str(partitionIndex) + ' updated array: ' + str(arr)

    return partitionIndex

'''
# Algorithms Week 3 Assignment
# CORRECT:
#   a) 162085
#   b) 164123
#   c) 138382
'''
'''
import sys
with open('TestData-QuickSort.txt') as f:
    data = f.read()

strArray = data.strip().split('\n')
intArray = [int(numStr) for numStr in strArray]

#count = [0]
print(quickSort(intArray,0,9999))
#print(intArray)
#print(count)
#'''

''' TEST CASES '''
'''
a = [3,4,1,8,6,2,9]
print(quickSort(a,0,6,0))
print str(a)

a = [9,4,1,8,6,2,3]
print(quickSort(a,0,6,0))
print str(a)

a = [1,2,3,4,5,6,7]
print(quickSort(a,0,6,0))
print str(a)

a = [7,6,5,4,3,2,1]
print(quickSort(a,0,6,0))
print str(a)

a = [1,2,3,4,1,6,7]
print(quickSort(a,0,6,0))
print str(a)

a = [9,9,3,1,5,6,7]
print(quickSort(a,0,6,0))
print str(a)

a = [1,2,3,4,-5,6,-6]
print(quickSort(a,0,6,0))
print str(a)
#'''
