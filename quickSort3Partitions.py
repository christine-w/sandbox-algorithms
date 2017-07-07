# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    pivot = a[l]
    leftPartitionIndex = l
    rightPartitionIndex = r
    for i in range(l + 1, r + 1):
        if i > rightPartitionIndex:
            break
        while a[i] > pivot:
            a[rightPartitionIndex], a[i] = a[i], a[rightPartitionIndex]
            rightPartitionIndex -= 1
        if a[i] < pivot:
            leftPartitionIndex += 1
            a[i], a[leftPartitionIndex] = a[leftPartitionIndex], a[i]
        #print('updated array: ' + str(a) + ' m1: ' + str(leftPartitionIndex) + ' m2: ' + str(rightPartitionIndex))
    a[l], a[leftPartitionIndex] = a[leftPartitionIndex], a[l]
    return leftPartitionIndex, rightPartitionIndex

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    #m = partition2(a, l, r)
    m1, m2 = partition3(a, l , r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);

#'''
a = [2, 3, 9, 2, 2]
randomized_quick_sort(a, 0, len(a)-1)
print(str(a))

a = [2, 1, 9, 2, 2]
randomized_quick_sort(a, 0, len(a)-1)
print(str(a))

a = [2, 1, 0, 2, 2]
randomized_quick_sort(a, 0, len(a)-1)
print(str(a))

a = [2, 1, 0, 2, 1, 2, 5, 1, 3]
randomized_quick_sort(a, 0, len(a)-1)
print(str(a))
#'''

''' assignment submission code for reading input
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
#'''
