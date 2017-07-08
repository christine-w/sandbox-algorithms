# python2
'''
quickSort.py
input: an array of integers
output: array of integers sorted in ascending order

quick sort has an average running time of O(nlogn)
'''
import random
import sys

def quickSort(arr, left, right, numComparisons):
    #print 'left: ' + str(left) + ' right: ' + str(right) + ' array: ' + str(arr)
    if left >= right:
        #print 'BASE CASE REACHED'
        return

    numComparisons[0] += right - left
    #print(right - left)
    #pivotIndex = random.randint(left, right)
    #pivotIndex = left      #question1
    pivotIndex = right     #question2
    '''
    medianIndex = (right - left)//2
    medianValue = sorted([arr[left], arr[left+medianIndex], arr[right]])[1]
    if arr[left] == medianValue:
        pivotIndex = left
    elif arr[left+medianIndex] == medianValue:
        pivotIndex = left + medianIndex
    else:
        pivotIndex = right
    '''
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
    #numComparisons[0] += partitionIndex - left - 1
    quickSort(arr, left, partitionIndex - 1, numComparisons)
    #print 'SORT RIGHT...',
    #numComparisons[0] += right - partitionIndex - 1
    quickSort(arr, partitionIndex + 1, right, numComparisons)

    return
'''
# Algorithms Week 3 Assignment
# Attempt 1:
#   a)
#
'''
'''
with open('TestData-QuickSort.txt') as f:
    data = f.read()

strArray = data.strip().split('\n')
intArray = [int(numStr) for numStr in strArray]

count = [0]
quickSort(intArray,0,9999, count)
#print(intArray)
print(count)
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
