## 简介
这是一个可以分割出fasta格式的脚本，可以把一个物种的中不同的基因序列找出来，生成不同的fasta文件。
也可以把不同物种相同的基因的进行聚类生成fasta格式的文件，方便序列比对，建树。

## 功能
- 分割序列
 把需要分割的源文件放入src文件夹中执行，程序会自动执行，执行完毕会在目录里生成bulid文件夹
```shell script
python split_sequence.py
```

- 聚类
把需要分割的源文件放入src文件夹中执行，执行完毕会在目录里生成bulid文件夹，默认为sequence
```shell script
python sort_sequence.py
```
     
