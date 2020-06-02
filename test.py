import jieba
s = "中国特色社会主义进入新时代，我国社会主要矛盾已经转化为人民日益增长的美好生活需要和不平衡不充分的发展之间的矛盾。"
n = len(s)
m = len(jieba.lcut(s))
print("中文字符数为{}，中文词语数为{}。".format(n, m))

print("二进制{0:b}、十进制{0}、八进制{0:o}、十六进制{0:x}".format(0x4DC0+50))

