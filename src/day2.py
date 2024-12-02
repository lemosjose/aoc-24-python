#site says i may be "unlucky because the part 2 is right for someone else, and i may be "unlucky". wtf."

def checkRules(arr, rule) -> str:

    if sequenceIsSafe(arr, rule):
        return "safe"

    safe_count = 0
    for i in range(len(arr)):
        testArray = arr[:i] + arr[i+1:]
        
        if sequenceIsSafe(testArray, rule):
            safe_count += 1

            if safe_count > 1:
                return "unsafe"

        

    return "safe" if safe_count == 1 else "unsafe"


def sequenceIsSafe(arr, rule):
    #i actually don't know if using this string check is the best way of taking apart each rule....
    if rule == "increasing":
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if diff <= 0 or diff > 3:
                return False
        return True
                
    
    elif rule == "decreasing":
        for i in range(len(arr) - 1):
            diff = arr[i] - arr[i + 1]
            if diff <= 0 or diff > 3:
                return False         
        return True
        
    
    
            
def input(file) -> int:
    safe_counter = 0
    with open(file, 'r') as f:
        for line in f:
            arr = list(map(int, line.split()))
            if arr[0] < arr[1]:
                #echange checkRules and checkNewRules for checking the difference
                if (checkRules(arr, "increasing")) == "safe":
                        safe_counter += 1
                    
            elif arr[0] > arr[1]:
                if (checkRules(arr, "decreasing")) == "safe":
                        safe_counter += 1
                    

    return safe_counter

print(input("../inputs/day2.txt"))
              
