import time
import threading
from bin.tools import *


def align(names):
    """
    调取核心比对序列
    """
    lock.acquire()
    readPath = "..\\bulid\\class\\use\\"
    outPath = "..\\bulid\\megax\\aligned\\"
    clustal_align_pro = "..\\mega_mao\\clustal_align_protein.mao"
    # clustal_align_pro = ".\\mega_mao\\clustal_align_nucleotide.mao"
    os.system("megacc -a {} -d {} -f Fasta -o {}".format(clustal_align_pro, readPath + names, outPath + names))
    lock.release()  # 释放锁
    threadmax.release()  # 释放信号量，可用信号量加一


if __name__ == '__main__':
    """
    实现多线程比对序列
    """
    start = time.time()
    threads = []
    readPath = "..\\bulid\\class\\use\\"
    thrNum = len(list_name(readPath))
    threadmax = threading.BoundedSemaphore(8)  # 限制线程的最大数量为4个
    lock = threading.Lock()  # 将锁内的代码串行化
    for i in range(thrNum):
        threadmax.acquire()  # 增加信号量，可用信号量减一
        t = threading.Thread(target=align, args=(list_name(readPath)[i],))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    end = time.time()
    print("执行用时{}".format(end - start))
