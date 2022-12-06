with open("day01/file.txt") as file:
    sum_list=[]
    templist=[]

    for line in file.readlines():
        if line == '\n':
            sum_list.append(sum(templist))
            templist=[]
        else:
            templist.append(int(line.strip('\n')))
        
    print(sum(sorted(sum_list, reverse=True)[:3]))