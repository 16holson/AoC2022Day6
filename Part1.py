import sys

def readFile():
    file = open("InputData.txt", "r")
    return file


def isUnique(string):

    char_set = [False] * 128

    for i in range(0, len(string)):

        val = ord(string[i])
        if char_set[val]:
            return False

        char_set[val] = True

    return True


def traverseLine(line, start):
    if(isUnique(line[start:(start+4)])):
        return start+4
    elif(start != (len(line)-4)):
        return traverseLine(line, start+1)


def main():
    file = readFile()
    sys.setrecursionlimit(2000)
    print(traverseLine(file.readline(), 0))
    file.close()

if (__name__ == "__main__"):
    main()
