import os


# def get_file_name(file_allname):
#     """
#     接收文件名称，包括后缀名称
#     返回：生成列表fasta, 和不包括后缀名的名称file_name
#     # file_allname = input("输入你要分析出的文件,包括后缀名\n")
#     """
#     try:
#         # file_allname = input("输入你要分析出的文件,包括后缀名\n")
#         p = file_allname.find(".")
#         file_name = file_allname[:p]
#         os.mkdir(".\\" + file_name)
#         f = open(file_allname).read()
#         fasta = f.split(">")
#         return fasta, file_name
#     except:
#         print("请正确输入文件名称。")


#
def file_name(file_allname):
    """
    传入文件的全名，返回文件的名称。
    :param file_allname:
    :return:
    """
    try:
        # file_allname = input("输入你要分析出的文件,包括后缀名\n")
        p = file_allname.find(".")
        file_name = file_allname[:p]
        return file_name
    except:
        print("请正确输入文件名称。")


def fasta(file_allname):
    """
    需要传入file_allname的路径
    :param file_allname:
    :return: 返回fasta格式的序列list
    """
    try:
        # file_allname = input("输入你要分析出的文件,包括后缀名\n")
        f = open(file_allname).read()
        fasta = f.split(">")
        return fasta
    except:
        print("请正确输入文件名称。")


def write_sequence_file(fasta, file_name="bulid"):
    """
    分析出序列，得出文件
    接收fasta列表，输出的文件夹名称
    :param fasta:
    :param file_name:
    :return: 在bulid中生成需要的sequence文件
    """
    # file_name = "Berchemia berchemiifolia"
    # if os.os.path.exists(file_name):
    #     pass
    # else:
    #     os.mkdir(file_name)
    for i in fasta:
        if i:
            i = ">" + i
            b = i.find("[gene=")
            c = i.find("] [locus_tag")
            gene_title = i[b + 6:c]
            sequence_name = file_name + "_" + gene_title + ".fasta"
            sequence_file = open('.\{}\{}'.format(file_name, sequence_name), 'w')
            sequence_file.write(i)
        # sequence_file.close()
        else:
            print("未写入{}".format(i))


def list_name():
    """
    获取文件列表，判断是否有src文件目录
    :return: 返回一个src目录中的所有文件名的列表
    """
    list_name = os.listdir(".\\src")
    return list_name
