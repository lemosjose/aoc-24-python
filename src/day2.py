#contains only part A for the day

#thanks, lerax!
def signum(x):
    return (x > 0) - (x < 0)


def checkRules(line: list[int]):
    levels = len(line) - 1
    ruled = [
        #will check if it's inscreasing or decreasing with signum
        signum(a - b) if abs(a - b) <= 3 else 0
        for a,b in zip(line, line[1:])
    ]
    return abs(sum(ruled)) == levels
    
    
    
            
def main(file) -> int:
            #filters the levels from each line to an int array
    lines = [list(map(int, line.split()))
             
            for line in open(file).readlines()]

    return len(list(filter(checkRules, lines)))
    


print(main("../inputs/day2.txt"))

