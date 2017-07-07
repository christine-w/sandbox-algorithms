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
    if left >= right:
        #print 'BASE CASE REACHED'
        return

    pivotIndex = random.randint(left, right)
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

    #print 'SORT LEFT...',
    quickSort(arr, left, partitionIndex - 1)
    #print 'SORT RIGHT...',
    quickSort(arr, partitionIndex + 1, right)

''' TEST CASES '''
#'''
a = [3,4,1,8,6,2,9]
quickSort(a,0,6)
print str(a)

a = [9,4,1,8,6,2,3]
quickSort(a,0,6)
print str(a)

a = [1,2,3,4,5,6,7]
quickSort(a,0,6)
print str(a)

a = [7,6,5,4,3,2,1]
quickSort(a,0,6)
print str(a)

a = [1,2,3,4,1,6,7]
quickSort(a,0,6)
print str(a)

a = [9,9,3,1,5,6,7]
quickSort(a,0,6)
print str(a)

a = [1,2,3,4,-5,6,-6]
quickSort(a,0,6)
print str(a)
#'''
