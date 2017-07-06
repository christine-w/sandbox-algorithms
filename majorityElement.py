# python2
'''
majorityElement.py
input: a list of positive integer elements of length n
output: 1 if there is a majority element (occurs more than n/2); 0 otherwise
'''
import sys

def getMajorityElement(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    
    midpoint = left + (right - left)//2
    #print 'midpoint: ' + midpoint
    
    leftMajority = getMajorityElement(a, left, midpoint)
    rightMajority = getMajorityElement(a, midpoint, right)
    
    leftMajorityCount = 0;
    rightMajorityCount = 0;
    for i in range(left, right):
        if a[i] == leftMajority:
            leftMajorityCount += 1
        elif a[i] == rightMajority:
            rightMajorityCount += 1
            
    if leftMajorityCount > (right - left)/2:
        return leftMajority
        
    if rightMajorityCount > (right - left)/2:
        return rightMajority        
        
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:]
    if getMajorityElement(a, 0, n) != -1:
        print 1
    else:
        print 0