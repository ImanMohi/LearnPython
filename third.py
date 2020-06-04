#get the name of the file and open it
name= input('Enter file: ')
handle=open(name,'r')

#count word frequency
counts=dict()
 for line in handle:
  words=line.split()
  for word in words:
   counts[word]=counts.get(word,0)+1
