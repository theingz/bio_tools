## 简介
这是一个可以分割出fasta格式的脚本，可以把一个物种的中不同的基因序列找出来，生成不同的fasta文件。
也可以把不同物种相同的基因的进行聚类生成fasta格式的文件，方便序列比对，建树。

## 功能
1. 分割序列

 把需要分割的源文件放入src文件夹中执行，程序会自动执行，执行完毕会在目录里生成bulid文件夹
```shell script
python split_seq.py
```
2. gene 聚类

把需要分割的源文件放入src文件夹中执行，执行完毕会在目录里生成bulid文件夹，默认名称为sequence
```shell script
python sort_seq.py
```
3. 自动标注

把已经有的csv文件，添加到source文件中命名为lable.csv，把对应的基因序列文件放在src文件夹中，在终端中执行命令
执行程序可在bulid文件夹中生成标注好的fasta格式的文件
```shell script
python autoLable_seq.py
```

**注意**
1. source为csv文件，格式如
```
accD,61098,62831,+
atpA,11306,12829,-
atpB,56556,58052,-
atpE,56158,56559,-
```
2. src中fasta文件未标注的序列中第一行标注结尾为"]"，没有请自行添加




