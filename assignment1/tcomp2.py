#########################################################
##  CS 4750 (Fall 2016), Assignment #1, Question #2    ##
##   Script File Name: tcomp2.py                       ##
##       Student Name: Adam Smith                      ##
##         Login Name: aes702                          ##
##              MUN #: 201036597                       ##
#########################################################

from __future__ import division
import sys

#########################
## nW(fileName)
## Input: fileName: file to generate unique words from
## return: set of unique words
#########################
def nW(fileName):
	#open file
	f = open(fileName, "r")
	words = set()
	#iterate throug each line
	for line in f:
		#split line into words
		for word in line.split():
			#if word not already in set, add to set
			if not word in words:
				words.add(word)

	#close file
	f.close()

	#return set
	return words

#########################
## SD(x, y)
## Input: x: word set 1
## y: word set 2
## return: return set difference
#########################
def SD(x, y):
	#count difference of x from y
	count = len(x.difference(y))
	#count difference of y from x
	count += len(y.difference(x))

	#return difference
	return count

#########################
## SD(x, y)
## Input: x: file1 to compare
## y: file 2 to compare
## return: return score between two files
#########################
def sim(x, y):
	#get set from file x
	words1 = nW(x);
	#get set from file y
	words2 = nW(y);
	# calculate and return difference
	return 1.0 - (SD(words1, words2) / (len(words1) + len(words2)))

#get arg count
argc = len(sys.argv)
#get inital compare file
file1 = sys.argv[1]

#setup to find best file
best = -1;
bestname = "none"

#loop through each arg
for i in range(2, argc):
	#compate files
	tmp = round(sim(file1, sys.argv[i]), 3)
	tmp += 0
	#print result
	print "Sim(\"" + file1 + "\", \"" + sys.argv[i] + "\") = {:.3f}".format(tmp)
	#set best if it is
	if tmp >= best:
		best=tmp
		bestname = sys.argv[i]

#print best file
print "File " + "\"" + file1 + "\" is most similar to file \"" + bestname + "\"."
