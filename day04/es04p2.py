with open("day04/file.txt") as file:

    counter=0
    templist=[]
    for line in file.readlines():
        templist=[int (x) for x in line.replace('-',' ').replace(',',' ').split()]
        x=range(templist[0], templist[1]+1)
        y=range(templist[2], templist[3]+1)
        if len(list(set(x) & set(y))) > 0:
            counter+=1
        
    print(counter)
