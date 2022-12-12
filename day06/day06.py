def part1():
    with open("day06/file.txt") as file:
        input_file, finish = file.readline(), 4
        for i in range(len(input_file)):
            substring=input_file[i:finish]
            sublist=set(substring)
            if len(substring) != len(sublist):
                finish+=1
            else:
                break
        
        return finish
        
print(part1())

def part2():
    with open("day06/file.txt") as file:
        input_file, finish = file.readline(), 14
        for i in range(len(input_file)):
            substring=input_file[i:finish]
            sublist=set(substring)
            if len(substring) != len(sublist):
                finish+=1
            else:
                break
        
        return finish

print(part2())