#converting words to vectors 
import csv
import numpy as np
import pandas as pd
from gensim.models import Word2Vec
fp= open("extracted_keywords", "r")
fq=open("training.csv","a+")
l=list()
r=list()
for line in fp.readlines():
	rank_split=line.split(",")
	rank_split[0]=rank_split[0].strip()
	list_keywords=rank_split[0].split(" ")
	l.append(list_keywords)
	r.append(rank_split[1].replace("\n",""))

k=0
model = Word2Vec(l, min_count=0)
p,q=[],[]
for i in l:
	for j in i:
		#fq.write(model[j]+"\t"+r[k]+"\n")		
		#writer = csv.writer(fq)
		#writer.writerows(model[j])
		t=np.concatenate((model[j]), axis=None).tolist()
		t.append(r[k])
		p.append(t)
		q.append(r[k])	
	k=k+1
df = pd.DataFrame(p).add_prefix('Col')
df.to_csv('/home/aakash/Desktop/pagerank/training.csv', index=False)
fp.close()
fq.close()			
	




  
