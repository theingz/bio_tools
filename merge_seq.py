from tools import *
import os


def write_sequence(fastList: list):
    for fast in fastList:
        if fast:
            fast = ">" + fast
            first = fast.find(">")
            last = fast.find("gene")
            sequence_index = fast.find("\n")
            fileName = fast[first + 1:last - 1]
            sequence = fast[sequence_index + 1:]
            sequence_file = open('.\\bulid\sort\{}'.format(fileName + ".fasta"), 'a')
            sequence_file.write(sequence)

        else:
            pass


def add_head(path=".\\bulid\sort\\"):
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
    srcPath = ".\\src\\sequence\\"
    bulidPath = ".\\bulid\sort\\"
    mkdir('.\\bulid\sort')
    for names in list_name(srcPath):
        file_allname = srcPath + names
        print("执行 " + names)
        fastaList = fasta(file_allname)
        write_sequence(fastaList)
    add_head(bulidPath)
    path_file_merge(bulidPath)
    print("已完成")
