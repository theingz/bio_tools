import os
# from tools import *

# file_allname = input("输入你要分析出的文件,包括后缀名\n")
# file_allname = "Berchemia lineata chloroplast.gb"
file_allname = ".\src\Berchemia berchemiifolia.gb"

def file_name():
    p = file_allname.find(".")
    file_name = file_allname[:p]
    return file_name

# 已写完
def get_file(file_allname):
    """
    获取文件,
    返回：生成列表fasta, 和不包括后缀名的名称file_name
    """
    try:
        # file_allname = input("输入你要分析出的文件,包括后缀名\n")
        p = file_allname.find(".")
        file_name = file_allname[:p]
        f = open(file_allname).read()
        fasta = f.split(">")
        return fasta, file_name
    except:
        print("请正确输入文件名称。")


# 已写完
def write_sequence_file(fasta, file_name):
    """分析出序列，得出文件
    接收fasta列表，文件夹名称
    """
    # file_name = "Berchemia berchemiifolia"
    mkdir(".\\bulid\{}".format(file_name))
    sequenceDict = {}
    a = 0
    for i in fasta:
        if i:
            a = a + 1
            i = ">" + i
            b = i.find("[gene=")
            c = i.find("[locus_tag")
            gene_title = i[b:c-1]
            # sequence_name = str(a) + "_" + file_name + "_" + gene_title + ".fasta"
            sequence_name = file_name + "_" + gene_title + ".fasta"

            # if gene_title in sequenceDict.keys():
            #     sequenceDict[gene_title] = sequenceDict[gene_title] + fasta[a]
            # else:
            #     sequenceDict[gene_title] = fasta[a]

            sequenceDict[gene_title] = fasta[a]


            sequence_file = open('.\\bulid\{}\{}'.format(file_name, sequence_name), 'w')
            sequence_file.write(i)

        else:
            print("未写入{}".format(i))
    print(a, len(sequenceDict.keys()))

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
        print("已有这个文件夹")


if __name__ == '__main__':
    """主函数 
    get_file()
    write_sequence_file()
    """
    fasta, file_name = get_file(file_allname)
    write_sequence_file(fasta, file_name)
