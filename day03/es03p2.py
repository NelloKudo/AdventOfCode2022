with open("day03/file.txt") as file:
    alphabet="0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    itemsum=0

    for rucksack in file.readlines():
        print(rucksack[:(len(rucksack)//2)])
        print(rucksack[(len(rucksack)//2):])
        for letter in rucksack[:len(rucksack)//2]:
            if letter in rucksack[len(rucksack)//2:]:
                print(letter)
                itemsum+=alphabet.index(letter)
                break

    print(itemsum)