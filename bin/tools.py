import os


def list_name(path="..\\source\\"):
    """
    获取文件列表，判断是否有src文件目录
    :return: 返回一个src目录中的所有文件名的列表
    """
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    else:
        pass
        # print("{}已存在".format(path))
    try:
        list_name = os.listdir(path)
        return list_name
    except:
        print("请正确放入文件到src文件夹中")


# 已完成,传入str全名(包括后缀)，返回str中间名
def file_name(file_allname: str):
    """
    传入文件的全名，返回文件的名称。
    :param file_allname:
    :return:
    """
    try:
        if "\\" in file_allname:
            # file_allname = input("输入你要分析出的文件,包括后缀名\n")
            q = file_allname.rfind(".")
            s = file_allname.rfind("\\")
            file_name = file_allname[s + 1:q]
            # print(q,s)
            return file_name
        else:
            q = file_allname.rfind(".")
            file_name = file_allname[:q]
            return file_name
    except:
        print("请正确输入文件名称。")


# 已完成，传入str全名，返回list,文件fasta格式的squence的list
def fasta(file_allname: str):
    """
    需要传入file_allname的路径
    :param file_allname:
    :return: 返回fasta格式的序列list
    """
    try:
        # file_allname = input("输入你要分析出的文件,包括后缀名\n")
        f = open(file_allname).read()
        fasts = f.split(">")
        fast_seq = []
        index = 0
        for fast in fasts:
            if fast:
                fast = ">" + fast
                fast_seq.append(fast)
                index = index + 1
        return fast_seq
    except:
        print("请正确输入文件名称。")


# 已完成，传入list,fast_squence,返回key为[gene],val为squence的字典。
def sequence_dict(fasta, fileName):
    """
    传入fasta的序列返回一个以gene和序列的映射字典
    :param fasta:
    :return:
    """
    sequenceDict = {}
    sameDict = {}
    index = 0
    same = 0

    for i in fasta:
        index = index + 1
        b = i.find("[gene=")
        c = i.find("[locus_tag")
        line_e = i.rfind("]")
        gene_key = i[b:c - 1]
        i = ">" + fileName + " " + gene_key + "\n" + i[line_e + 1:].replace("\n", "") + "\n"
        if i and gene_key:
            if gene_key in sequenceDict.keys():
                sameDict[gene_key] = sequenceDict[gene_key] + i
                same = same + 1
            else:
                sequenceDict[gene_key] = i
        else:
            pass
            # print("字段为空未写入字典{}，忽略此提示".format(i))
    key_len = len(sequenceDict.keys())
    same_gene_list = sameDict.keys()
    print("一共找到" + str(key_len) + "个基因序列", "有{}".format(same) + "个为相同")
    print("相同基因分别为{}\n".format(same_gene_list))
    return sequenceDict


# 已完成，不更改序列名
def sequence_dict_2(fasta):
    """
    传入fasta的序列返回一个以gene和序列的映射字典
    :param fasta:
    :return:
    """
    for names in list_name():
        file_allname = ".\src" + names
        sequenceDict = {}
        index = 0
        same = 0
        fileName = file_name(file_allname)
        for i in fasta:
            if i:
                index = index + 1
                b = i.find("[gene=")
                c = i.find("[locus_tag")
                line_e = i.rfind("]")
                gene_key = i[b:c - 1]
                i = fileName + gene_key + i[line_e + 1:]
                if gene_key in sequenceDict.keys():
                    sequenceDict[gene_key] = sequenceDict[gene_key] + i
                    same = same + 1
                else:
                    sequenceDict[gene_key] = i
            else:
                print("字段为空未写入{}".format(i))
        key_len = len(sequenceDict.keys())
        print("一共找到" + str(key_len) + "个基因", "有{}".format(same) + "为相同，以舍去")
        return sequenceDict


# 已写完，用这个需要传入字典和不包括后缀的名称名，
def write_sequence_file(sequenceDict, path="..\\bulid\\cluster\\", fileName="sequence", findSeqNaem=True):
    """
    接收一个字典，
    """
    # fileName = "Berchemia berchemiifolia"
    # sequenceDict = {}
    items = sequenceDict.items()
    mkdir(path)
    a = 0
    if items:
        for fastas in sorted(items):
            sequence = fastas[1]
            gene = "_" + fastas[0]
            if sequence and findSeqNaem:
                a = a + 1
                # sequence_name = str(a) + "_" + fileName + "_" + gene_title + ".fasta"
                sequence_name = fileName + gene + ".fasta"
                sequence_file = open(path + sequence_name, 'w')
                sequence_file.write(sequence)
            else:
                sequence_name = fastas[0] + ".fasta"
                sequence_file = open(path + sequence_name, 'w')
                sequence_file.write(sequence)
                pass
                # print("序列为空，未写入文件，{}".format(sequence))
        print("{}已写入到 bulid 文件夹中\n".format(fileName))
    else:
        print("序列为空，未写入文件")


# 已写完，看需求可用
def write_sequence_file2(fasta, file_name="bulid"):
    """
    分析出序列，得出文件
    接收fasta列表，输出的文件夹名称
    :param fasta:
    :param file_name:
    :return: 在bulid中生成需要的sequence文件
    """
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


# 已写完，接收一个dict的list,返回大的dict
def big_dict(list):
    """
    接收一个dict的list,返回大的dict
    """
    seqInfo = []
    bigDict = {}
    for dicts in list:
        for keys in dicts.keys():
            if keys in bigDict.keys():
                bigDict[keys] = bigDict[keys] + dicts[keys]
                seqInfo.append(str(len(bigDict[keys])) )
            else:
                bigDict[keys] = dicts[keys]
                seqInfo.append(str(len(bigDict[keys])) )
    # seqInfo_csv = open('.\\dataInfor\\aut_sort\{}'.format("seqInfo.csv"), 'a')
    # seqInfo_csv.write(",".join(seqInfo) + "\n")

    return bigDict

def seq_infor(list):
    """
    接收一个dict的list字典，返回大字典的信息。
    """


# autoLable_seq.py
def write_merge(dict, fileName="sequence"):
    """
    传入字典，和文件名称
    合并一个字典的所有值为一个文件
    """

    # dictw = {}
    big_str = ""
    mkdir(".\\bulid\{}".format(fileName))
    for gene in sorted(dict.keys()):
        big_str = big_str + dict[gene] + "\n"
    sequence_name = fileName + ".fasta"
    sequence_file = open('.\\bulid\{}\{}'.format(fileName, sequence_name), 'w')
    sequence_file.write(big_str)


# 合并文件夹中的文件为一个大文件
def path_file_merge(path):
    if "allsequence.fas" in list_name(path):
        pass
    else:
        for names in list_name(path):
            file_allname = path + names
            myStr = open(file_allname).read()
            sequence_file2 = open('{}\\{}'.format(path, "allsequence.fas"), 'a')
            sequence_file2.write(myStr)


# 创建文件夹，传入path路径，
def mkdir(path):
    """
    创建文件夹
    file = "G:\\xxoo\\test"
    mkdir(file)
    """
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    else:
        print("{}已存在，内容以修改".format(path))
