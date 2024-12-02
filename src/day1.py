from collections import Counter

leftArray = []
rightArray = []


def input(file):
    with open(file, 'r') as f:
        for line in f:
            left, right = map(int, line.split())
            leftArray.append(left)
            rightArray.append(right)
            
def calc(left, right):
    sumDifferences = 0
    for i,j in zip(left, right):
        sumDifferences += abs(i - j)
    return sumDifferences 

def similarity(left, right):
    totalCount = 0
    for i in left:
        count = counter_right.get(i, 0)
        totalCount += i*count

    return totalCount
        

input("../inputs/day1.txt")
leftArray, rightArray = sorted(leftArray), sorted(rightArray)
print(calc(leftArray, rightArray))
counter_right = Counter(rightArray)
print(similarity(leftArray, rightArray))
    

            
        
