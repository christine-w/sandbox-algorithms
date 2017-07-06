# mcountInversions.py
# input: an array of integers
# output: number of inversions that were in the array
#
# inversions count how many moves are needed to move out-of-place elements into an ordered list
# for example, in the list [3, 2, 1], 3 is two places out of place so that's two inversions; once 3 is in place, 1 is one out of place
# so the total is 3 inversions
def countInversions(arr):
    """Leverage merge sort to find number of inversions in a list"""
    if len(arr) == 1:
        #print('BASE CASE REACHED')
        return 0, arr
    
    midpoint = len(arr)//2
    leftCount, leftArray = countInversions(arr[:midpoint])
    rightCount, rightArray = countInversions(arr[midpoint:])
    #print('--- DIVIDE AND CONQUER ---')
    #print('len: ' + str(len(arr)) + ' midpoint: ' + str(midpoint) + ' leftArray: ' + str(leftArray) + ' leftCount: ' + str(leftCount) + ' rightArray: ' + str(rightArray) + ' rightCount: ' + str(rightCount))
    
    leftIndex = 0
    rightIndex = 0
    sortedArray = []
    inversionCount = leftCount + rightCount
    #print('--- MERGE SOLUTIONS ---')
    for i in range(len(arr)):
        #print('i: ' + str(i) + ' leftIndex: ' + str(leftIndex) + ' rightIndex: ' + str(rightIndex) + ' inversionCount: ' + str(inversionCount))
        if leftArray[leftIndex] <= rightArray[rightIndex]:
            sortedArray.append(leftArray[leftIndex])
            leftIndex += 1
            #print('left index incremented, now: ' + str(leftIndex) + ' inversionCount: ' + str(inversionCount))
        else:
            sortedArray.append(rightArray[rightIndex])
            rightIndex += 1
            inversionCount += len(leftArray) - leftIndex
            #print('right index incremented, now: ' + str(rightIndex) + ' inversionCount: ' + str(inversionCount))
        #print('sortedArray: ' + str(sortedArray))
        if leftIndex == len(leftArray):
            #print('left array used up! just append rest of right array to result. inversionCount: ' + str(inversionCount))
            sortedArray += rightArray[rightIndex:]
            break
        if rightIndex == len(rightArray):
            #print('right array used up! just append rest of left array to result. inversionCount: ' + str(inversionCount))
            sortedArray += leftArray[leftIndex:]
            break
    
    return inversionCount, sortedArray 
    
#print(countInversions([3,2,1]))
#print(countInversions([1,3,5,2,4,6]))

# Algorithms Week 2 Assignment
# Attempt 1: 2397819672 (Issue: array of strings had to be converted to array of ints first)
# Attempt 2: 2407905288 CORRECT Answer
with open('TestData-CountInversions.txt') as f:
    data = f.read()

strArray = data.strip().split('\n')
intArray = [int(numStr) for numStr in strArray]

count, sortedArray = (countInversions(intArray))
print(str(count))
#print(sortedArray)