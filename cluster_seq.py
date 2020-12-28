from tools import *

if __name__ == '__main__':
    """主函数
    get_file()
    write_sequence_file()
    """
    dictList = []
    path = ".\\src\\"
    for names in list_name(path):
        fileAllname = ".\src\\" + names
        print("执行 " + names)
        fileName = file_name(fileAllname)
        fast = fasta(fileAllname)
        dict = sequence_dict(fast, fileName)
        dictList.append(dict)
    bigDict = big_dict(dictList)
    write_sequence_file(bigDict)
    print("已完成")
