from tools import *

# file_allname = input("输入你要分析出的文件,包括后缀名\n")
# print(fileName)
# bigDict = {}

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
        write_sequence_file(dictw, fileName)
    print("已完成")
