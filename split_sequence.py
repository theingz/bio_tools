import os, re
from tools import *

# file_allname = input("输入你要分析出的文件,包括后缀名\n")

# print(fileName)
# bigDict = {}


# 已写完，需要传入字典和不包括后缀的名称名，
def write_sequence_file(sequenceDict, fileName):
    """分析出序列，得出文件
    接收fasta列表，文件夹名称
    """
    # fileName = "Berchemia berchemiifolia"
    # sequenceDict = {}
    items = sequenceDict.items()
    mkdir(".\\bulid\{}".format(fileName))
    a = 0
    for fastas in items:
        sequence = fastas[1]
        gene = fastas[0]
        if sequence:
            a = a + 1
            # sequence = ">" + sequence
            line_s = sequence.find(">")
            line_e = sequence.rfind("]")
            sdfs = sequence[line_s:line_e]
            # print(sdfs)
            # sequence_name = str(a) + "_" + fileName + "_" + gene_title + ".fasta"
            sequence_name = fileName + "_" + gene + ".fasta"

            sequence_file = open('.\\bulid\{}\{}'.format(fileName, sequence_name), 'w')
            sequence_file.write(sequence)
        else:
            pass
            # print("序列为空，未写入文件，{}".format(sequence))
    print("{}已写入到 bulid 文件夹中\n".format(fileName))


if __name__ == '__main__':
    """主函数
    get_file()
    write_sequence_file()
    """
    for names in list_name():
        file_allname = ".\src\\"+ names
        print("执行 " + names)
        fileName = file_name(file_allname)
        fast = fasta(file_allname)
        dict = sequence_dict(fast, fileName)
        write_sequence_file(dict, fileName)
    print("已完成")


