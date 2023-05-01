

def find_ways_count(matrix: list, width: int, height: int):

    squares = [[] for i in range(width)]
    for row in range(height):
        squares[0].append(1)

    memoization = {}
    for row in range(height):
        memoization.setdefault(matrix[row][0], 0)
        memoization[matrix[row][0]] += 1

    for column in range(1, width):
        ways = {}

        for row in range(height):
            square = matrix[row][column]
            memoization.setdefault(square, 0)

            if square is not matrix[row][column-1]:
                way = squares[column - 1][row] + memoization[square]
            else:
                way = memoization[square]

            ways[square] = ways.get(square, 0) + way
            squares[column].append(way)

        for k in ways:
            memoization[k] += ways[k]

    if height == 1:
        return squares[width-1][0]
    return squares[width-1][0] + squares[width-1][height-1]


def main():
    with open('ijones.in', 'r') as ijones:
        width, height = map(int, ijones.readline().split())

        matrix = []
        for i in range(height):
            matrix.append(ijones.readline().rstrip('\n'))

    with open('ijones.out', 'w') as ijones:
        ijones.write(str(find_ways_count(matrix, width, height)))


if __name__ == '__main__':
    main()
