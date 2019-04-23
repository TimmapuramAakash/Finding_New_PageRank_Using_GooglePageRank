#!/usr/bin/python
import re  
from urllib.parse import urlparse, parse_qs

# Open a file
fo = open("training_set", "r")
file=open("extracted_keywords","w+")
l=list()
while(True):
	line = fo.readline()
	lines=line.split(",")
	
	line=lines[0]
	
	#rank_line=lines[1]
	if(line==""):
		break
	else:	
		line1=lines[1]
		parsed_url = urlparse(line)
		if(len(parsed_url.path)>1):
			remove_extension= re.sub(r'\..*', '', parsed_url.path)
			get_keywords=re.split(r'/',remove_extension)
			keywords=get_keywords[1:]
			
		if(len(parse_qs(parsed_url.query))):
			for k,v in parse_qs(parsed_url.query).items():
					if(v[0]!=''):
						l.append(v[0])
			
		if(len(parse_qs(parsed_url.query))>1 and len(parsed_url.path)>1):
			if(len(str(l+keywords))>3):
				result1=""
				for i in l+keywords:
					result1=result1+" "+i
					file.write(result1+","+line1)
				##file.write(l+keywords+list(line1))
		elif(len(parsed_url.path)>1):	
			if(len(str(keywords))>3):
				result2=""
				for i in keywords:
					result2=result2+" "+i
					file.write(result2+","+line1)
				
		else:
			if(len(str(l))>3):
				result=""
				for i in l:
					result=result+" "+i
					file.write(result+","+line1)
		l.clear()

# Close opend file
fo.close()
file.close()
'''
with open("extracted_keywords","r") as fd:
	skip_line=fd.readlines()
with open("extracted_keywords","w+") as fg:
	fg.write(str(skip_line[1:]))'''

