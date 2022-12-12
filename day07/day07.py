# This one definitely needed me to look up for solutions online lol,
# people are crazy good at this. Gonna make a try with dictionaries as
# I still struggle with other stuff..

def part1():
    
    def dictionary_paths_check(path, dictionary):
        if path not in dictionary.keys():
            dictionary[path] = 0
        return dictionary

    with open ("day07/file.txt") as file:
        data = file.readlines()

        size_dictionary={}
        current_path=""
        current_dir_files=[]

        for line in data:
            if line.startswith("$ cd"):
                if line.strip() == "$ cd /":
                    current_path="/"
                    current_dir_files=["/"]
                    size_dictionary=dictionary_paths_check(current_path, size_dictionary)

                elif line.strip() == "$ cd ..":
                    current_dir_files.pop()
                    current_path='/'.join(current_path.split("/")[:-1])

                elif not line.startswith("$ cd /") and not line.startswith("$ cd .."):
                    if current_path != "/":
                        current_path+="/" + line.split()[-1]
                    else:
                        current_path += line.split()[-1]
                    current_dir_files.append(current_path)
                    size_dictionary = dictionary_paths_check(current_path, size_dictionary)

            if line[0].isdigit():
                file_size = int(line.split()[0])
                for directory in current_dir_files:
                    size_dictionary[directory] += file_size

    return sum([value for value in size_dictionary.values() if value <= 100000])
    
print(part1())

def part2():
    
    def dictionary_paths_check(path, dictionary):
        if path not in dictionary.keys():
            dictionary[path] = 0
        return dictionary

    with open ("day07/file.txt") as file:
        data = file.readlines()

        size_dictionary={}
        current_path=""
        current_dir_files=[]

        for line in data:
            if line.startswith("$ cd"):
                if line.strip() == "$ cd /":
                    current_path="/"
                    current_dir_files=["/"]
                    size_dictionary=dictionary_paths_check(current_path, size_dictionary)

                elif line.strip() == "$ cd ..":
                    current_dir_files.pop()
                    current_path='/'.join(current_path.split("/")[:-1])

                elif not line.startswith("$ cd /") and not line.startswith("$ cd .."):
                    if current_path != "/":
                        current_path+="/" + line.split()[-1]
                    else:
                        current_path += line.split()[-1]
                    current_dir_files.append(current_path)
                    size_dictionary = dictionary_paths_check(current_path, size_dictionary)

            if line[0].isdigit():
                file_size = int(line.split()[0])
                for directory in current_dir_files:
                    size_dictionary[directory] += file_size

    root_size=size_dictionary["/"]
    delete_size=root_size-40000000

    return min([value for value in size_dictionary.values() if value >= delete_size])

print(part2())