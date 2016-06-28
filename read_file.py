#
# basic code for reading file in line by line
#

# change as needed
FILE_NAME = "input.txt"

# main method
def main():
    readFile()

def readFile():
    # open file
    file = open(FILE_NAME, "r")

    # parse file
    # loops over each line in file
    for line in file:
        parseLine(line)

    # close file
    file.close()

# pares the line by looping over each character
def parseLine( line ):
    for c in line:
        parseInput(c)

def parseInput( input ):
    # code goes here
    print ( input )

if __name__ == "__main__":
    main()
