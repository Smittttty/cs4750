#########################################################
##  CS 4750 (Fall 2016), Assignment #1, Question #2    ##
##   Script File Name: tcomp2.py                       ##
##       Student Name: Adam Smith	                   ##
##         Login Name: aes702                          ##
##              MUN #: 201036597                       ##
#########################################################

from __future__ import division
import sys

file1 = "tc1.dat"
file2 = "tc2.dat"

def nW(fileName):
	f = open(fileName, "r")
	words = set()
	for line in f:
		for word in line.split():
			if not word in words:
				words.add(word)
	return words

def SD(x, y):
	count = len(x.difference(y))
	count += len(y.difference(x))		
	
	return count
	
def sim(x, y):
	words1 = nW(x);
	words2 = nW(y);
	
	return 1.0 - (SD(words1, words2) / (len(words1) + len(words2)))
	
argc = len(sys.argv)
file1 = sys.argv[1]	
best = -1;
bestname = "none"

for i in range(2, argc):
	tmp = round(sim(file1, sys.argv[i]), 3)
	tmp += 0
	print "Sim(\"" + file1 + "\", \"" + sys.argv[i] + "\") = {:.3f}".format(tmp)#round(tmp, 3))
	if tmp >= best:
		best=tmp
		bestname = sys.argv[i]

print "File " + "\"" + file1 + "\" is most similar to file \"" + bestname + "\"."