import os


def list_name():
    """
    获取文件列表，判断是否有src文件目录
    :return: 返回一个src目录中的所有文件名的列表
    """
    list_name = os.listdir(".\\src")
    return list_name


# 已完成
def file_name(file_allname):
    """
    传入文件的全名，返回文件的名称。
    :param file_allname:
    :return:
    """
    try:
        # file_allname = input("输入你要分析出的文件,包括后缀名\n")
        q = file_allname.rfind(".")
        s = file_allname.rfind("\\")
        file_name = file_allname[s + 1:q]
        # print(q,s)
        return file_name
    except:
        print("请正确输入文件名称。")


# 已完成
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


# 已完成，用这个
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
        if i:
            index = index + 1
            # i = ">" + i
            b = i.find("[gene=")
            c = i.find("[locus_tag")
            # line_s = i.find(">")
            line_e = i.rfind("]")
            # i[line_s+2:line_e-1] = "theing"
            # print(i)
            gene_key = i[b:c - 1]
            i = ">" + fileName + gene_key + i[line_e + 1:]
            # print(i)
            # i[line_s:line_e] = "> {} {}".format(fileName, gene_key)
            if gene_key in sequenceDict.keys():
                sameDict[gene_key] = sequenceDict[gene_key] + i
                # sameDict[gene_key] = i
                same = same + 1
            else:
                sequenceDict[gene_key] = i
        else:
            pass
            # print("字段为空未写入字典{}，忽略此提示".format(i))
    key_len = len(sequenceDict.keys())
    same_gene_list = sameDict.keys()
    print("一共找到" + str(key_len) + "个基因序列", "有{}".format(same) + "个为相同，以舍去")
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
                # i = ">" + i
                b = i.find("[gene=")
                c = i.find("[locus_tag")
                # line_s = i.find(">")
                line_e = i.rfind("]")
                # i[line_s+2:line_e-1] = "theing"
                # print(i)
                gene_key = i[b:c - 1]
                i = fileName + gene_key + i[line_e + 1:]
                print(i)
                # i[line_s:line_e] = "> {} {}".format(fileName, gene_key)
                if gene_key in sequenceDict.keys():
                    # sequenceDict[gene_key] = sequenceDict[gene_key] + i
                    same = same + 1
                else:
                    sequenceDict[gene_key] = i
            else:
                print("字段为空未写入{}".format(i))
        key_len = len(sequenceDict.keys())
        print("一共找到" + str(key_len) + "个基因", "有{}".format(same) + "为相同，以舍去")
        return sequenceDict


# 已写完，用这个需要传入字典和不包括后缀的名称名，
def write_sequence_file(sequenceDict, fileName="sequence"):
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
            # sequence_name = str(a) + "_" + fileName + "_" + gene_title + ".fasta"
            sequence_name = fileName + "_" + gene + ".fasta"
            sequence_file = open('.\\bulid\{}\{}'.format(fileName, sequence_name), 'w')
            sequence_file.write(sequence)
        else:
            pass
            # print("序列为空，未写入文件，{}".format(sequence))
    print("{}已写入到 bulid 文件夹中\n".format(fileName))


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


def dict_list():
    dictList = []
    for names in list_name():
        file_allname = ".\src\\" + names
        print("执行 " + names)
        fileName = file_name(file_allname)
        fast = fasta(file_allname)
        dict = sequence_dict(fast, fileName)
        dictList.append(dict)
    return dictList


def big_dict(list):
    bigDict = {}
    for i_dict in list:
        # print(i_dict)
        for i in i_dict.keys():
            # print(i)
            if i in bigDict.keys():
                bigDict[i] = bigDict[i] + i_dict[i]
            else:
                bigDict[i] = i_dict[i]
    # for i in bigDict.items():
    #     print(i)
    return bigDict


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
        print("{}已存在".format(path))
