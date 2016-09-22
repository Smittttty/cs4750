#########################################################
##  CS 4750 (Fall 2016), Assignment #1, Question #1    ##
##   Script File Name: tcomp1.py                       ##
##       Student Name: Adam Smith                      ##
##         Login Name: aes702                          ##
##              MUN #: 201036597                       ##
#########################################################

from __future__ import division
import sys

#########################
## Sim(X, Y)
## Input: n: ngram size
## x: file1 to compare
## y: file2 to compare
## return: ngram simulatity of two files.
#########################
def sim(n, x, y):
	## calculate and return score
	return getScoreFromDicts(getFileHistogram(n, x), getFileHistogram(n, y))

#########################
## getFileHistogram(n, fileName)
## Input: n: ngram size
## fileName: file name to generate ngram for
## return: ngram histogram for file
#########################
def getFileHistogram(n, fileName):
	# initalize histogram
	fHistogram = {}
	# initalize ngram count
	nGrams = 0;

	#open file and cycle through lines
	f = open(fileName)
	for line in f:
		#check that we have a valid ngram length
		if len(line) < n:
			continue
		#split line into word
		words = line.split()
		#cycle through words and generate ngram histogram for each word.
		for i in range(len(words)):
			getNGram(fHistogram, n, words[i])

	#calculate total number of nGrams
	for value in fHistogram.values():
		nGrams += value

	#calculate score
	for key, value in fHistogram.items():
		fHistogram[key] = value/nGrams

	#close file
	f.close()
	return fHistogram

#########################
## getNGram(histogram, size, str)
## Input: histogram: histogram to write result to
## size: size of each nGram
## str: string to search ngrams in
## return: histogram, numbr of ngrams in str
#########################
def getNGram(histogram, size, str):
	if(len(str) < size):
		return

	#iterate through string
	for i in range(0, len(str) - (size-1)):
		tmp = ""
		#create ngram key based off current n chars of string
		for k in range(size):
			tmp += str[i + k]
		#add to histogram
		if(histogram.has_key(tmp)):
			histogram[tmp] += 1
		else:
			histogram[tmp] = 1

	return histogram, (len(str) - (size-1))

#########################
## getScoreFromDicts(dict1, dict2)
## Input: dict1: dict1 to compare
## dict2: dict2 to compare
## return: score between two dicts
#########################
def getScoreFromDicts(dict1, dict2):
	score = 0.0
	#cycle through each value
	for key, value in dict2.items():
		# calculate difference and add to score
		if dict1.has_key(key):
			score += abs(value-dict1[key])
		else:
			score += value
	#cycle through dict1 and look for left over keys
	for key in dict1.keys():
		#add to score if not already added
		if not dict2.has_key(key):
			score += dict1[key]

	#calculate and return score.
	return 1-(score/2)


#get arg count
argc = len(sys.argv)
#get ngram size
n = int(sys.argv[2])
#get compate file
file1 = sys.argv[1]

#store best file
best = -1;
bestname = "none"

#loop through remaining files
for i in range(3, argc):
	##alculate score, +=0 is to fix negative 0.
	tmp = round(sim(n, file1, sys.argv[i]), 3)
	tmp += 0
	#print file store
	print "Sim(\"" + file1 + "\", \"" + sys.argv[i] + "\") = {:.3f}".format(tmp)
	#check if most similar file so far
	if tmp >= best:
		best=tmp
		bestname = sys.argv[i]

#print most similar file.
print "File " + "\"" + file1 + "\" is most similar to file \"" + bestname + "\"."
