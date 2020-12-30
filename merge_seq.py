from tools import *
import os


def write_sequence(fastList: list, path):
    for fast in fastList:
        if fast:
            # fast = ">" + fast
            first = fast.find(">")
            last = fast.find("gene")
            sequence_index = fast.find("\n")
            fileName = fast[first + 1:last - 1]
            sequence = fast[sequence_index + 1:]
            sequence_file = open('{}{}'.format(path, fileName + ".fasta"), 'a')
            sequence_file.write(sequence)
        else:
            pass


def add_head(path=".\\bulid\\marge\\"):
    for files in list_name(path):
        fileName = file_name(files)
        allSequence = open(path + files).read()
        if ">" in allSequence:
            continue
        else:
            newAllSequence = ">{}".format(fileName) + "\n" + allSequence
            sequence_file = open(path + files, 'w')
            sequence_file.write(newAllSequence)


if __name__ == '__main__':
    readPath = ".\\bulid\\cluster\\use\\"
    outPath = ".\\bulid\\marge\\"
    mkdir(outPath)
    listName = list_name(readPath)
    for names in listName:
        if os.path.isfile(readPath+names):
            file_allname = readPath + names
            print("执行 " + names)
            fastaList = fasta(file_allname)
            write_sequence(fastaList, outPath)
    add_head(outPath)
    path_file_merge(outPath)
    print("已完成")
