with open("day04/file.txt") as file:
    
    counter=0
    templist=[]
    for line in file.readlines():
        templist=[int (x) for x in line.replace('-',' ').replace(',',' ').split()]
        if templist[0] <= templist[2] and templist[1] >= templist[3]:
            counter+=1
        elif templist[2] <= templist[0] and templist[3] >= templist[1]:
            counter+=1
    
    print(counter)