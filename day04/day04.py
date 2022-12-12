def part1():
    with open("day04/file.txt") as file:
    
        counter=0
        templist=[]
        for line in file.readlines():
            templist=[int (x) for x in line.replace('-',' ').replace(',',' ').split()]
            if templist[0] <= templist[2] and templist[1] >= templist[3]:
                counter+=1
            elif templist[2] <= templist[0] and templist[3] >= templist[1]:
                counter+=1
    
    return counter

print(part1())

def part2():
    with open("day04/file.txt") as file:

        counter=0
        templist=[]
        for line in file.readlines():
            templist=[int (x) for x in line.replace('-',' ').replace(',',' ').split()]
            x=range(templist[0], templist[1]+1)
            y=range(templist[2], templist[3]+1)
            if len(list(set(x) & set(y))) > 0:
                counter+=1
        
    return counter

print (part2())
