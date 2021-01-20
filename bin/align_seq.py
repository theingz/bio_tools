import time
from threading import Thread
from bin.tools import *


def align(names):
    """
    调取核心比对序列
    """
    readPath = "..\\bulid\\cluster\\use\\"
    outPath = "..\\bulid\\megax\\aligned2\\"
    clustal_align_pro = "..\\mega_mao\\clustal_align_protein.mao"
    # clustal_align_pro = ".\\mega_mao\\clustal_align_nucleotide.mao"
    os.system("megacc -a {} -d {} -f Fasta -o {}".format(clustal_align_pro, readPath + names, outPath + names))


if __name__ == '__main__':
    """
    实现多线程比对序列
    """
    start = time.time()
    threads = []
    readPath = "..\\bulid\\cluster\\use\\"
    thrNum = len(list_name(readPath))
    for i in range(thrNum):
        t = Thread(target=align, args=(list_name(readPath)[i],))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    end = time.time()
    print("执行用时{}".format(end - start))
