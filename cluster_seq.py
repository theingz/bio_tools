from tools import *


def use_sequence(readPath, outPath):
    mkdir(outPath + "\\use")
    for file in list_name(outPath):
        if os.path.isfile(outPath + file):
            fileName = file_name(file)
            fast = open(outPath + file).read()
            geneLen = fast.count(">")
            fListLen = len(list_name(readPath))
            if geneLen == fListLen:
                sequence_file = open('{}\\use\\{}'.format(outPath, file), 'w')
                sequence_file.write(fast)


if __name__ == '__main__':
    """主函数
    get_file()
    write_sequence_file()
    """
    dictList = []
    readPath = ".\\src\\"
    outPath = ".\\bulid\\cluster\\"
    for names in list_name(readPath):
        fileAllname = readPath + names
        print("执行 " + names)
        fileName = file_name(fileAllname)
        fast = fasta(fileAllname)
        dict = sequence_dict(fast, fileName)
        dictList.append(dict)
    bigDict = big_dict(dictList)
    write_sequence_file(bigDict, outPath)
    use_sequence(readPath, outPath)
    print("已完成")
