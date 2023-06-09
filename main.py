
def sort_by_tribes(pairs):

    found_tribe = -1
    tribes = []

    for pair in pairs:
        human1, human2 = pair
        if not tribes:
            tribes.append([human1, human2])
        else:
            for tribe in tribes:
                if human1 in tribe:
                    tribe.append(human2)
                    found_tribe = 1
                elif human2 in tribe:
                    tribe.append(human1)
                    found_tribe = 1

            if found_tribe == -1:
                tribes.append([human1, human2])
        found_tribe = -1

    return tribes


def count_possible_pairs(pairs):

    count = 0

    tribes = sort_by_tribes(pairs)
    boys = {}
    girls = {}
    for tribe in tribes:
        tribe_index = tribes.index(tribe)
        boys[tribe_index] = 0
        girls[tribe_index] = 0
        for human in tribe:
            if human % 2 == 0:
                boys[tribe_index] += 1
            else:
                girls[tribe_index] += 1

    for i in range(len(tribes) - 1):
        for j in range(i + 1, len(tribes)):
            count += boys[i]*girls[j] + boys[j]*girls[i]

    return count


def main():
    pairs = []

    with open('input.txt', 'r') as file:
        lines = file.readlines()
        num = int(lines[0].strip())
        for line in lines[1:]:
            human1, human2 = map(int, line.strip().split(' '))
            pairs.append((human1, human2))

    with open('output,txt', 'w') as file:
        file.write(str(count_possible_pairs(pairs)))


if __name__ == '__main__':
    main()
