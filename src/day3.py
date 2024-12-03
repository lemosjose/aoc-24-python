import re

#i'm using arrays to be 

#part B
#using re.findall instead cuz why not....
def parseDoDontMul():

    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, open("../inputs/day3.txt").read())


    #control the enabling
    flag = True
    #thank you, reddit.
    res = 0

    for match in matches:
        if match == "do()":
            flag = True
        elif match == "don't()":
            flag = False
        else:
            if flag:
                x, y = map(int, match[4:-1].split(","))
                res += x * y

    return res

    
#part A
def parseMul(inputList):
    res = 0 
    
    for i in inputList:
        matches = re.finditer(r'mul\((\d+),(\d+)\)', i)

        for match in matches:
            x,y = map(int, (match.group(1), match.group(2)))
            res += x*y

    return res 

def main():

    #part A stuff
    lines = [line.strip()
             for line in open("../inputs/day3.txt")]

    #answer for part A and B
    return(f"{parseMul(lines)} \n {parseDoDontMul()}")



    


print(main())

