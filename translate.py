'''import csv
file=open('rench_dictionary.csv','r')
reader=csv.reader(file)
dic={}
for i in reader:
    dic[i[0]]={'fre':i[1]}'''

'''import csv  
filename ='french_dictionary.csv'
with open(filename, 'r') as data:   
    for line in csv.DictReader(data): 
        print(line)'''

#import fileinput
import pandas as pd
import re
def replace_words(text, word_dic):
    rc = re.compile('|'.join(map(re.escape, word_dic)))
    def translate(match):
        return word_dic[match.group(0)]
    return rc.sub(translate, text)
fin = open('t8.shakespeare.txt', "r")
str2 = fin.read()
fin.close()
word_dic=pd.read_csv('french_dictionary.csv', header=None, index_col=0, squeeze=True).to_dict()
str3 = replace_words(str2, word_dic)
print(str3)
fout = open('find_words.txt', "w")
fout.write(str3)
fout.close()



