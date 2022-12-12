def part1():
    with open("day03/file.txt") as file:
        alphabet="0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        itemsum=0
        for rucksack in file.readlines():
            for letter in rucksack[:len(rucksack)//2]:
                if letter in rucksack[len(rucksack)//2:]:
                    itemsum+=alphabet.index(letter)
                    break

    return itemsum

print(part1())

def part2():
    with open("day03/file.txt") as file:
        alphabet="0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        itemsum=0
        line_counter=0
        rucksack_list=[]

        for rucksack in file.readlines():
            line_counter+=1
            if line_counter == 3:
                rucksack_list.append(rucksack.strip('\n'))
                for rucksack in rucksack_list:
                    for letter in rucksack:
                        if letter in rucksack_list[1] and letter in rucksack_list[2]:
                            itemsum+=alphabet.index(letter)
                            break
                    break
                rucksack_list=[]
                line_counter=0
            else:
                rucksack_list.append(rucksack.strip('\n'))

    return itemsum

print(part2())