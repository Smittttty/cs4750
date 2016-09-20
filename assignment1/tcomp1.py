#########################################################
##  CS 4750 (Fall 2016), Assignment #1, Question #1    ##
##   Script File Name: tcomp1.py                       ##
##       Student Name: Adam Smith                      ##
##         Login Name: aes702                          ##
##              MUN #: 201036597                       ##
#########################################################

from __future__ import division
import sys

def sim(x, y):
	return getScoreFromDicts(getFileHistogram(n, x), getFileHistogram(n, y))

def getFileHistogram(n, fileName):
	fHistogram = {}
	nGrams = 0;

	f = open(fileName)
	for line in f:
		if len(line) < n:
			continue
		words = line.split()
		for i in range(len(words)):
			getNGram(fHistogram, n, words[i])

	for value in fHistogram.values():
		nGrams += value
		
	for key, value in fHistogram.items():
		fHistogram[key] = value/nGrams
	
	f.close()
	return fHistogram
		
def getNGram(histogram, size, str):
	for i in range(0, len(str) - (size-1)):
		tmp = ""
		for k in range(size):
			tmp += str[i + k]
		if(histogram.has_key(tmp)):
			histogram[tmp] += 1 
		else:
			histogram[tmp] = 1

	return histogram, (len(str) - (size-1))

def getScoreFromDicts(dict1, dict2):
	score = 0.0
	for key, value in dict2.items():
		if dict1.has_key(key):
			score += abs(value-dict1[key])
		else:
			score += value

	for key in dict1.keys():
		if not dict2.has_key(key):
			score += dict1[key]

	return 1-(score/2)


argc = len(sys.argv)
n = int(sys.argv[2])
file1 = sys.argv[1]	
best = -1;
bestname = "none"

for i in range(3, argc):
	tmp = round(sim(file1, sys.argv[i]), 3)
	tmp += 0
	print "Sim(\"" + file1 + "\", \"" + sys.argv[i] + "\") = {:.3f}".format(tmp)
	if tmp >= best:
		best=tmp
		bestname = sys.argv[i]

print "File " + "\"" + file1 + "\" is most similar to file \"" + bestname + "\"."

