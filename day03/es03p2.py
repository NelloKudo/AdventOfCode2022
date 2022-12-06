with open("day03/file.txt") as file:
    alphabet="0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    itemsum=0
    line_counter=0
    rucksack_list=[]

    for rucksack in file.readlines():
        line_counter+=1
        if line_counter != 4:
            rucksack_list.append(rucksack.strip('\n'))
        else:
            print (rucksack_list)
            for rucksack in rucksack_list:
                for letter in rucksack:
                    if letter in rucksack_list[1] and letter in rucksack_list[2]:
                        print(letter)
                        itemsum+=alphabet.index(letter)
                        break
                break
            rucksack_list=[]
            line_counter=0

    print(itemsum)