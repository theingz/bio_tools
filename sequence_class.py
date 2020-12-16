import os
from tools import *

# 获取文件名列表
list_name = os.listdir(".\\src")
print(list_name)


# def file_dict():
#     for i in list_name:
#         fasta_list = fasta(".\\src\\" + i)
#         name = file_name(i)
#         write_sequence_file(fasta_list)
#
#         # print(fasta_list)
#         # write_sequence_file(fast, i)
#
#
# list_sdf()


# 已完成，未测试
def get_geneindex(fasta):
    """
    接收列表，找到gene的的类别
    :return: gene在列表中的index,以gene为键可以是字典的形式
    """
    index = 0
    dict = {}
    for i in fasta:
        i = ">" + i
        b = i.find("[gene=")
        c = i.find("] [locus_tag")
        gene_title = i[b + 6:c]
        index = index + 1
        dict[gene_title] = index
    return dict

# ## 未完成
# def get_all_sequence(file_list_name):
#     """
#     获取所有的物种序列，并生成各自的基因序列字典
#     :return:
#     """
#     big_dict = {}
#     for i in file_list_name:
#         fasta, flie_name = get_file(i)
#         dict = get_geneindex(fasta, flie_name)
#
#
# if __name__ == '__main__':
#     fasta, file_name = get_file()
#     dect = get_geneindex(fasta, file_name)
# list_sdf()
