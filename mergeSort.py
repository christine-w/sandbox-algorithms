# mergeSort.py
# input: an array of integers
# output: array of integers sorted in ascending order
#
# merge sort has a running time of O(nlogn)
def mergeSort(arr):
    """Sort arr using merge sort"""
    if len(arr) == 1:
        #print('BASE CASE REACHED')
        return arr
    
    midpoint = len(arr)//2
    left = mergeSort(arr[:midpoint])
    right = mergeSort(arr[midpoint:])
    #print('--- DIVIDE AND CONQUER ---')
    #print('len: ' + str(len(arr)) + ' midpoint: ' + str(midpoint) + ' left: ' + str(left) + ' right: ' + str(right))
    
    leftIndex = 0
    rightIndex = 0
    sortedArray = []
    #print('--- MERGE SOLUTIONS ---')
    for i in range(len(arr)):
        #print('i: ' + str(i) + ' leftIndex: ' + str(leftIndex) + ' rightIndex: ' + str(rightIndex))
        if left[leftIndex] <= right[rightIndex]:
            sortedArray.append(left[leftIndex])
            leftIndex += 1
            #print('left index incremented, now: ' + str(leftIndex))
        else:
            sortedArray.append(right[rightIndex])
            rightIndex += 1
            #print('right index incremented, now: ' + str(rightIndex))
        #print('sortedArray: ' + str(sortedArray))
        if leftIndex == len(left):
            #print('left array used up! just append rest of right array to result')
            sortedArray += right[rightIndex:]
            break
        if rightIndex == len(right):
            #print('right array used up! just append rest of left array to result')
            sortedArray += left[leftIndex:]
            break
    
    return sortedArray   

# mergeSortTest.py
# input: length of list and range of values for test
# output: PASS or FAIL
#
# test correctness of merge sort implementation by comparing to built-in sort function      
def mergeSortTest(listLength, valueRange):
    import random
    testArray = []
    for i in range(listLength):
        testArray.append(int((random.uniform(-1,1)*valueRange)//1))
    
    sortedArray_model = sorted(testArray)
    sortedArray_test = mergeSort(testArray)
    
    if (sortedArray_test == sortedArray_model):
        print('PASSED. testArray: ' + str(testArray) + ' sortedArray_test: ' + str(sortedArray_test))
    else:
        print('FAILED. testArray: ' + str(testArray) + ' sortedArray_test: ' + str(sortedArray_test))
    
    
mergeSortTest(4, 10)
mergeSortTest(7, 50)
mergeSortTest(50, 25)
mergeSortTest(100, 100)
mergeSortTest(1000, 500)