import string
s="Shub#ha!m Ku)nal"
transtab = str.maketrans("", "", string.punctuation)
print(s.translate(transtab))