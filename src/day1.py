from collections import Counter

leftArray = []
rightArray = []


def createArrays(input):
    for line in input:
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
        

lines = [line.strip()
         for line in open("../inputs/day1.txt").readlines()]


createArrays(lines)
leftArray, rightArray = map(lambda x: sorted(x), (leftArray, rightArray))

print(calc(leftArray, rightArray))
counter_right = Counter(rightArray)

print(similarity(leftArray, rightArray))



            
        
