antonyms=dict()
new=dict()
while True:
	print ("enter a word")
	word=input()
	if word in antonyms:
		print ("the antonym of "+word+" is "+antonyms[word])
	else:
		print ("i don't know the antonym of "+word+"\ndo you know?")
		opt=input()
		if opt=="y":
			print ("what is it?")
			new[word]=input()
			antonyms.update(new)
			print (new)
			print (antonyms)
