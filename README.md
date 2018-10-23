# Finding_New_PageRank_Using_GooglePageRank
Google Page Ranking is used to find the rank of each page and now we training them on neural network to find the new  page rank.Many attributes are to taken to get  precise rank of new page but here i,m using url keywords and then  encoding them using glove and train.
check out page ranking code https://github.com/Chepkeitany/pagerank to assign rank for a page 
We have to execute according to readme only change is done in sprank.py
we need to add the below code in the program to get the url with their rank

# Get all url with page rank
cur.execute('''SELECT url,new_rank FROM Pages''')
file = open('training_set','w+')
for row in cur:
	file.write(str(row[0]) +','+ str(row[1])+'\n')
file.close()

Now we have our dataset next we have to clean and process it to train on neural network.
