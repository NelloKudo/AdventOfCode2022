with open("day02/file.txt") as file:
    moves_list=[]
    for line in file.readlines():
        moves_list.append(line.split())
    
    player_points=0

    for round in moves_list:
        elf=round[0]
        player=round[1]

        if elf == 'A':
            if player == 'X':
                player_points+=3+1
            elif player == 'Y':
                player_points+=6+2
            elif player == 'Z':
                player_points+=3

        if elf == 'B':
            if player == 'X':
                player_points+=1
            elif player == 'Y':
                player_points+=3+2
            elif player == 'Z':
                player_points+=6+3

        if elf == 'C':
            if player == 'X':
                player_points+=1+6
            elif player == 'Y':
                player_points+=2
            elif player == 'Z':
                player_points+=3+3

    print (player_points)




