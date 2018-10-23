# Finding_New_PageRank_Using_GooglePageRank
Google Page Ranking is used to find the rank of each page and now we training them on neural network to find the new  page rank.Many attributes are to taken to get  precise rank of new page but here i,m using url keywords and then  encoding them using glove and train.

check out page ranking code https://github.com/Chepkeitany/pagerank to assign rank for a page.
We have to execute all programs accordingly to get ranking for pages.
Only change is to be done in sprank.py and we need to add the below code in the program to get the url with rank of that page.

# Get all url with page rank( Training dataset)
cur.execute('''SELECT url,new_rank FROM Pages''')
file = open('training_set','w+')
for row in cur:
	file.write(str(row[0]) +','+ str(row[1])+'\n')
file.close()

We  will get training_set.txt

Now we have our dataset next we have to clean and process it to train on neural network.
# Extracting keywords from url
Run  test.py to get extracted_keywords_test.txt
# Encoding keywords using Word2vec 
Run word_to_vec.py to get the processed dataset that is cleaned_dataset.csv
# Train the model on neural network 
Run training_PR.py to get the trained model and save it for prediction.


