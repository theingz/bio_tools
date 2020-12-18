from tools import *
import sys


## 核心算法

# 缺少标记好的字典

def get_lable_list():
    """
    找到lable.csv文件
    : 返回list [['accD', '61098', '62831', '+'], ['atpA', '11306', '12829', '-']]
    """
    try:
        file = open(".\source\lable.csv")
        ls = []
        for line in file:
            line = line.replace("\n", "")
            ls.append(line.split(","))
        # print(ls)
        return ls
    except:
        mkdir(".\source")
        print("请在source文件夹中放入lable.csv文件")
        sys.exit()


## 已写完，传入文件路径，得到他的整个序列。可能会有很多bug
def full_sequence(file_allname):
    """
    接收文件路径，文件为整条序列
    返回一个，整理后的整条序列
    """
    # file = open("zi.fasta").read()

    file = open(file_allname).read()
    line = file.rfind("]")
    sequencea = file[line + 2:]
    seq = sequencea.replace("\n", "")
    return seq


# def dict(full_sequence: str, sour_list: list,fileName:str):
def dict(full_sequence: str, lable_list):
    """
    传入整条序列，和对应的lable的序列
    ：返回基因和序列的字典
    """
    sequenceDict = {}
    sameDict = {}
    same = 0
    transline = full_sequence[::-1].replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g').upper()

    for i in lable_list:
        if i[0]:
            gene_key = "[gene={}]".format(i[0])
            first = int(i[1]) - 1
            last = int(i[2])
            li_for = i[3]
            # print(gene_key, first, last, li_for)
            if li_for == "+":
                i = ">" + fileName + " " + gene_key + " [locus_tag=theing]" + "\n" + full_sequence[first:last]
                if gene_key in sequenceDict.keys():
                    sequenceDict[gene_key] = sequenceDict[gene_key] + "\n" + i
                    sameDict[gene_key] = sequenceDict[gene_key] + i
                    same = same + 1
                else:
                    sequenceDict[gene_key] = i
            elif li_for == "-":
                i = ">" + fileName + " " + gene_key + " [locus_tag=theing]" + "\n" + transline[first:last]
                if gene_key in sequenceDict.keys():
                    sequenceDict[gene_key] = sequenceDict[gene_key] + "\n" + i
                    sameDict[gene_key] = sequenceDict[gene_key] + i
                    same = same + 1
                else:
                    sequenceDict[gene_key] = i
            else:
                pass
        else:
            pass
    # print(dict)
    key_len = len(sequenceDict.keys())
    same_gene_list = sameDict.keys()
    print("一共找到" + str(key_len) + "个基因序列", "有{}".format(same) + "个为相同")
    print("相同基因分别为{}\n".format(same_gene_list))
    return sequenceDict


if __name__ == '__main__':
    for names in list_name():
        file_allname = ".\src\\" + names
        print("执行 " + names)
        fileName = file_name(file_allname)
        fullSequence = full_sequence(file_allname)
        dictw = dict(fullSequence, get_lable_list())
        wite_merge(dictw, fileName)
    print("已完成")
