import os
from tools import *

# 未完成
# def get_all_sequence(file_list_name):
#     """
#     获取所有的物种序列，并生成各自的基因序列字典
#     :return:
#     """
#     big_dict = {}
#     for i in file_list_name:
#         fasta, flie_name = get_file(i)
#         dict = get_geneindex(fasta, flie_name)


if __name__ == '__main__':
    """主函数
    get_file()
    write_sequence_file()
    """
    dictList = []
    for names in list_name():
        file_allname = ".\src\\" + names
        print("执行 " + names)
        fileName = file_name(file_allname)
        fast = fasta(file_allname)
        dict = sequence_dict(fast, fileName)
        dictList.append(dict)
    bigDict = big_dict(dictList)
    write_sequence_file(bigDict)

print("已完成")
