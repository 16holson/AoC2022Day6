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
    if(isUnique(line[start:(start+14)])):
        print(f"Found Unique: {line[start:(start+14)]}")
        return start+14
    elif(start != (len(line)-14)):
        print(f"Not Unique: {line[start:(start + 14)]}")
        return traverseLine(line, start+1)


def main():
    file = readFile()
    sys.setrecursionlimit(1000)
    line = file.readline()
    for i in range(len(line)):
        if(isUnique(line[i:(i+14)]) and len(line[i:(i+14)]) == 14):
            print(i+14)



if (__name__ == "__main__"):
    main()