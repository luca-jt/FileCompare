from sys import argv
from os.path import isfile

# change the inputFile.. variables for actual use:
# inputFile1 = argv[1]
# inputFile2 = argv[2]
inputFile1 = "testfile1.txt"
inputFile2 = "testfile2.txt"

outputFile = "diff.patch"

if not isfile(inputFile1) or not isfile(inputFile2):
    raise ValueError("Invalid file paths.")

diff = ["diff\n", "--- " + inputFile1 + " | +++" + inputFile2 + "\n"]


def add_to_diff(line: str, sign=" "):
    diff.append(sign + " " + line)


def index_if_line_contained(lines: list[str], line: str, index=0) -> int:
    for i in range(index, len(lines)):
        if lines[i] == line:
            return i
    return 0


def parse_changes(d: list[str]):
    with open(outputFile, 'w') as out:
        for i in d:
            out.write(i)


def main():

    with open(inputFile1) as f1:
        file1 = f1.readlines()

        with open(inputFile2) as f2:
            file2 = f2.readlines()

            i = j = 0
            while i < len(file1) or j < len(file2):

                line1 = file1[i] if i < len(file1) else ""
                line2 = file2[j] if j < len(file2) else ""

                if line1 != line2:

                    if (found_index := index_if_line_contained(file2, line1, j)) > 0:
                        for k in range(j, found_index):
                            add_to_diff(file2[k], sign="+")
                            j = found_index

                    elif (found_index := index_if_line_contained(file1, line2, i)) > 0:
                        for k in range(i, found_index):
                            add_to_diff(file1[k], sign="-")
                            i = found_index

                    else:
                        add_to_diff(line2, sign="+")
                        j += 1
                        add_to_diff(line1, sign="-")
                        i += 1

                else:
                    add_to_diff(line1)
                    i += 1
                    j += 1

            parse_changes(diff)


if __name__ == "__main__":
    main()
