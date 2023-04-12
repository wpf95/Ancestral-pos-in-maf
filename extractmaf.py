# time：2023/4/11 16:52
# name：Wangpf
# encoding：utf-8

#usage:python extractmaf.py [maf.file] [out.file]

import sys
maf=open(sys.argv[1],"r")
outfile=open(sys.argv[2],"w")

list1 = []

for line in maf:
    if line.startswith("s") :
        line1 = line.rstrip().split()
        list1.append(line1)
for r in [list1[i:i + 2] for i in range(0, len(list1), 2)]:  # 列表生成式
    start_pos=int(r[0][2])
    chrom=r[0][1].split(".")[1]
    num=int(max(r[0][3],r[1][3]))
    seq1 = r[0][6].upper()
    seq2 = r[1][6].upper()
    l = -1
    if r[0][1] != r[1][1]:
        for i in range(num):
            if seq1[i] == "-":  #先判断“-”，因为他和不等是相同的，要提前写出来
                l = l + 0
            elif seq1[i] != seq2[i]:
                l = l + 1
            elif seq1[i] == seq2[i]:
                l = l + 1
                end_pos = start_pos + l
                outfile.write(chrom+"\t"+str(end_pos)+"\t"+seq1[i]+"\n")
maf.close()
outfile.close()
