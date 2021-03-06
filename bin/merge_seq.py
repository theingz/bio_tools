from tools import *
import os
import sys

def name_seq_dict(fastList: list):
    seqDict = {}
    csv2 = ['']
    a = 0
    for fast in sorted(fastList):
        a = a + 1
        if fast:
            # fast = ">" + fast
            first = fast.find(">")
            last = fast.find("gene")
            sequence_index = fast.find("\n")
            fileName = fast[first + 1:last - 1]
            sequence = fast[sequence_index + 1:].replace("\n", "").replace(" ", "").replace("\t", "").replace("\r", "")
            seqLen = len(sequence)
            csv2.append(str(seqLen))
            # inforList = [sequence, seqLen]
            # seqDict[fileName] = inforList
            if fileName in seqDict.keys() and sequence and fileName:
                seqDict[fileName] = seqDict[fileName] + sequence
            else:
                seqDict[fileName] = sequence
        else:
            pass
    # sequence_svc2 = open('.\\dataInfor\\aut_sort\{}'.format("sequence2.csv"), 'a')
    # sequence_svc2.write(",".join(csv2) + "\n")
    return seqDict

def add_head(path="..\\bulid\\marge\\"):
    """
    添加头信息头，
    """
    for files in sorted(list_name(path)):
        fileName = file_name(files)
        allSequence = open(path + files).read()
        if ">" in allSequence:
            continue
        else:
            newAllSequence = ">{}".format(fileName) + "\n" + allSequence + "\n"
            sequence_file = open(path + files, 'w')
            sequence_file.write(newAllSequence)


if __name__ == '__main__':

    readPath = "..\\bulid\\megax\\aligned\\"
    outPath = "..\\bulid\\merged\\aligned\\"
    mkdir(outPath)
    listName = list_name(readPath)
    dictList = []
    for names in listName:
        if os.path.isfile(readPath + names) and "fasta" in names:
            file_allname = readPath + names
            print("执行 " + names)
            fastaList = fasta(file_allname)
            dictList.append(name_seq_dict(fastaList))
        else:
            pass
    # seqInfo_csv = open('.\\dataInfor\\aut_sort\{}'.format("seqInfo.csv"), 'a')
    # seqInfo_csv.write(",".join(seqInfo) + "\n")

    bigDict = big_dict(dictList)
    write_sequence_file(bigDict, outPath, findSeqNaem=False)
    add_head(outPath)
    path_file_merge(outPath)
    print("内容已写入{}文件夹，打开 allsequence.fas 即可".format(outPath))
    print("已完成")
