from tools import *


def find(path, findStr):
    a = 0
    print(list_name(path))
    for names in list_name(path):
        pathName = path + names
        if findStr in open(pathName).read():
            a = a + 1
            # print(pathName)
        else:
            print(pathName)
    print(a)


if __name__ == '__main__':
    path = ".\\src\\sequence\\"
    findStr = "Amborella_trichopoda"
    find(path, findStr)
