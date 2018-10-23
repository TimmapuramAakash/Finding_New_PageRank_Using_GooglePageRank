#converting words to vectors 
#import csv
from gensim.models import Word2Vec
fp= open("extracted_keywords_test", "r")
fq=open("training.csv","w+")
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
for i in l:
	for j in i:
		#fq.write(model[j]+"\t"+r[k]+"\n") 
		
		#writer = csv.writer(fq)
		#writer.writerows(model[j])
		
		print(model[j],r[k])
	k=k+1
	


fp.close()
fq.close()			
	




  
