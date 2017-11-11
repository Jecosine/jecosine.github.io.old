import re
import sys


keywords=["and","as","assert","break","class","continue","def","del","elif","else","except","exec","False","finally","for","from","global","if","import","in","is","lambda","None","not","or","pass","print","raise","return","True","try","while","with","yield","async","await"]

pyfile=open(sys.argv[1],'r')
content = pyfile.read()
words = content.split(' ')
html=""
for word in words:
	for key in keywords:
		if word.find(key) is not -1:
			html+=word[:word.find(key)]+"<strong>"+word+"</strong>"+word[word.find(key):]+" "
			break
		else:
			continue
	html+=word+" "
print html