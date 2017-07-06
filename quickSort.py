# python2
'''
quickSort.py
input: an array of integers
output: array of integers sorted in ascending order

quick sort has an average running time of O(nlogn)
'''
import random
import sys

def quickSort(arr, left, right):
    #print 'left: ' + str(left) + ' right: ' + str(right) + ' array: ' + str(arr)
    if right - left == 1:
        #print 'BASE CASE REACHED'
        return arr

    pivotIndex = random.randint(left, right)
    pivotIndex = left
    if pivotIndex != left:
        arr[left], arr[pivotIndex] = arr[pivotIndex], arr[left]
    #print 'pivot: ' + str(arr[left]) + ' pivotIndex: ' + str(pivotIndex) + ' new array: ' + str(arr)

    partitionIndex = left + 1
    for i in range(left + 1, right):
        if arr[i] <= arr[left]:
            if i != partitionIndex:
                arr[partitionIndex], arr[i] = arr[i], arr[partitionIndex]
            partitionIndex += 1
    arr[left], arr[partitionIndex - 1] = arr[partitionIndex - 1], arr[left]
    #print 'partitionIndex: ' + str(partitionIndex) + ' updated array: ' + str(arr)

    if partitionIndex > left + 1:
        #print 'SORT LEFT...',
        quickSort(arr, left, partitionIndex - 1)
    if partitionIndex < right:
        #print 'SORT RIGHT...',
        quickSort(arr, partitionIndex, right)

    return arr

''' TEST CASES '''
#'''
print quickSort([3,4,1,8,6,2,9],0,7)
print quickSort([9,4,1,8,6,2,3],0,7)
print quickSort([1,2,3,4,5,6,7],0,7)
print quickSort([7,6,5,4,3,2,1],0,7)
print quickSort([1,2,3,4,1,6,7],0,7)
print quickSort([9,9,3,1,5,6,7],0,7)
print quickSort([1,2,3,4,-5,6,-6],0,7)
#'''
