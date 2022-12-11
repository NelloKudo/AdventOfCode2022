with open ("day05/file.txt") as file:
    
    crates_list=[]
    for line in file.readlines()[:9]:
        

        pass

    for line in file.readlines()[10:]:
        moves_list=line.split()
        crates_num, start, finish=int(moves_list[1]), int(moves_list[3]), int(moves_list[5])


        print(moves_list)   