from typing import Optional


def create_temporary_array(pattern: str):
    pattern_len = len(pattern)
    temporary_array = [0] * len(pattern)

    j = 0
    i = 1
    while i < pattern_len:
        if pattern[j] == pattern[i]:
            temporary_array[i] = j + 1
            i += 1
            j += 1
        else:
            if j != 0:
                j = temporary_array[j - 1]
            else:
                temporary_array[i] = 0
                i += 1

    return temporary_array


def kmp_search(string: str, pattern: str) -> Optional[int]:
    string_len = len(string)
    pattern_len = len(pattern)
    temporary_array = create_temporary_array(pattern)

    i = 0
    j = 0
    while i < string_len:

        if string[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = temporary_array[j - 1]

        if j == pattern_len:
            return i - pattern_len

    return None


def main():
    string = input("Enter the string: ")
    pattern = input("Enter the pattern: ")
    print(kmp_search(string, pattern))


if __name__ == '__main__':
    main()
