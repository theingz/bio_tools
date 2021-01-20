from bin.tools import *


# file_allname = input("输入你要分析出的文件,包括后缀名\n")
# print(fileName)
# bigDict = {}

def write_merge(dict, fileName="sequence"):
    """
    基因为key , 序列为值的字典，和文件名称
    合并一个字典的所有值为一个文件
    """
    # dictw = {}
    locus_tag = " [locus_tag=theing]"
    big_str = "> " + fileName + locus_tag + "\n"
    mkdir("..\\bulid\\aut_sort")
    csv = [fileName] + sorted(list(dict.keys()))
    csv2 = [fileName]
    # disuse_str = "[gene=atpF],[gene=atpH],[gene=infA],[gene=lhbA],[gene=ndhA],[gene=ndhD],[gene=ndhE],[gene=ndhF],[gene=ndhG],[gene=ndhH],[gene=ndhI],[gene=ndhJ],[gene=ndhK],[gene=petL],[gene=psaI],[gene=psbL],[gene=psbM],[gene=psbZ],[gene=rps16],[gene=rps19],[gene=ycf15],[gene=ycf1],[gene=ycf68],[gene=rrn16],[gene=rrn23],[gene=rrn4.5],[gene=rrn5],[gene=trnA-UGC],[gene=trnC-GCA],[gene=trnD-GUC],[gene=trnE-UUC],[gene=trnF-GAA],[gene=trnG-GCC],[gene=trnG-UCC],[gene=trnH-GUG],[gene=trnI-CAU],[gene=trnI-GAU],[gene=trnK-UUU],[gene=trnL-CAA],[gene=trnL-UAA],[gene=trnL-UAG],[gene=trnM-CAU],[gene=trnN-GUU],[gene=trnP-UGG],[gene=trnQ-UUG],[gene=trnR-ACG],[gene=trnR-UCU],[gene=trnS-GCU],[gene=trnS-GGA],[gene=trnS-UGA],[gene=trnT-GGU],[gene=trnT-UGU],[gene=trnV-GAC],[gene=trnV-UAC],[gene=trnW-CCA],[gene=trnY-GUA],[gene=trnfM-CAU]"
    disuse_str = "[gene=atpH]	[gene=infA]	[gene=lhbA]	[gene=ndhA]	[gene=ndhD]	[gene=ndhE]	[gene=ndhF]	[gene=ndhG]	[gene=ndhH]	[gene=ndhI]	[gene=ndhJ]	[gene=ndhK]	[gene=petD]	[gene=petL]	[gene=psaI]	[gene=psbL]	[gene=psbM]	[gene=psbZ]	[gene=rps16]	[gene=rrn16]	[gene=rrn23]	[gene=rrn4.5]	[gene=rrn5]	[gene=ycf15]	[gene=ycf68]	[gene=rrn16S]	[gene=rrn23S]	[gene=rrn4.5S]	[gene=rrn5S]"

    disuse = disuse_str.split("\t")
    for gene in sorted(dict.keys()):
        # locus_tag = " [locus_tag=theing]"
        # gene_key = "[gene={}]".format(gene[0])
        # head = ">" + fileName + " " + gene_key + locus_tag + "\n"
        if gene in disuse or gene.find("trn")+1 or gene.find("tRN")+1:
            pass
        else:
            big_str = big_str + dict[gene]
            csv2.append(gene)
    sequence_name = fileName + ".fasta"
    sequence_file = open('..\\bulid\\aut_sort\{}'.format(sequence_name), 'w')
    sequence_file2 = open('..\\bulid\\aut_sort\{}'.format("allsequence.fas"), 'a')
    sequence_svc = open('..\\dataInfor\\aut_sort\{}'.format("sequence.csv"), 'a')
    sequence_svc2 = open('..\\dataInfor\\aut_sort\{}'.format("sequence2.csv"), 'a')
    sequence_file.write(big_str)
    sequence_file2.write(big_str+"\n")
    sequence_svc.write(",".join(csv) + "\n")
    sequence_svc2.write(",".join(sorted(csv2))+"\n")


# def sort_seq_all(dict,fileName):

def out_head(dict: dict):
    for i in dict.items():
        gene_key = i[0]
        first = i[1].find("<")
        last = i[1].rfind("]")
        gene_sequence = i[1][last + 2:].replace("\n", "")
        dict[gene_key] = gene_sequence
    return dict


if __name__ == '__main__':
    """主函数
    get_file()
    write_sequence_file()
    """
    for names in list_name():
        file_allname = "..\\source\\" + names
        print("执行 " + names)
        fileName = file_name(file_allname)
        fast = fasta(file_allname)
        dictw = sequence_dict(fast, fileName)
        outHeadDict = out_head(dictw)
        write_merge(outHeadDict, fileName)
    print("已完成")
