def part1():
    with open ("day05/file.txt") as file:
    
        input_data=file.readlines()

        crates_list= [ [] for s in range(11)]
        for line in input_data[:8]:
            for chars in range(0, len(line)-3, 4): 
                if line[chars] + line[chars+1] + line[chars+2] != '   ':
                        crates_list[chars//3].append(line[chars] + line[chars+1] + line[chars+2])
        
        crates_list.remove([])
        crates_list.remove([])

        for crate in crates_list:
            crate.reverse()
            
        moves_list=[]
        for line in input_data[10:]:
            moves_list.append(line.split())

        for move in moves_list:
            crates_num, start, finish=int(move[1]), int(move[3]), int(move[5])
            for _ in range(crates_num):
                crate=crates_list[start-1][-1]
                crates_list[finish-1].append(crate)
                crates_list[start-1].pop()

        result=''.join(crate[1] for crate in [crates_list[i][-1] for i in range(len(crates_list))])

    return result

print(part1())

def part2():
    with open ("day05/file.txt") as file:
    
        input_data=file.readlines()

        crates_list= [ [] for s in range(11)]
        for line in input_data[:8]:
            for chars in range(0, len(line)-3, 4): 
                if line[chars] + line[chars+1] + line[chars+2] != '   ':
                        crates_list[chars//3].append(line[chars] + line[chars+1] + line[chars+2])
        
        crates_list.remove([])
        crates_list.remove([])

        for crate in crates_list:
            crate.reverse()
            
        moves_list=[]
        for line in input_data[10:]:
            moves_list.append(line.split())

        for move in moves_list:
            crates_num, start, finish=int(move[1]), int(move[3]), int(move[5])
            crate_multiple_list= []
            for _ in range(crates_num):
                crate=crates_list[start-1][-1]
                crate_multiple_list.append(crate)
                crates_list[start-1].pop()
            crate_multiple_list.reverse()
            for crate2 in crate_multiple_list:
                crates_list[finish-1].append(crate2)

        result=''.join(crate[1] for crate in [crates_list[i][-1] for i in range(len(crates_list))])

    return result

print(part2())