#########################################################
##  CS 4750 (Fall 2016), Assignment #1, Question #3    ##
##   Script File Name: index1.py                       ##
##       Student Name: Adam Smith	                   ##
##         Login Name: aes702                          ##
##              MUN #: 201036597                       ##
#########################################################

from __future__ import division
import sys
import string
import collections

def loadIgnoreList(fileName):
	f = open(fileName, "r")
	words = set()
	
	for line in f:
		for word in line.split():
			words.add(word)
	
	f.close()
	
	return words
	
def getLineNumbers(ignored, fileName):
	lines = {}
	f = open(fileName, "r")
	lineNumber = 1
	for line in f:
		for word in line.split():
			#word = word.lower()
			word = word.translate(None, string.punctuation)
			if not len(word) > 0:
				continue
			if not word in ignored:
				if not lines.has_key(word):
					lines[word] = str(lineNumber) + " "
				else:
					lines[word] += str(lineNumber) + " "
		lineNumber += 1
			
	return lines

ignored = sys.argv[1]
text = sys.argv[2]
output = sys.argv[3]
	
lines = getLineNumbers(loadIgnoreList(ignored), text)
sortedLines = collections.OrderedDict(sorted(lines.items()))

f = open(output, "w")

for key, value in sortedLines.items():
	f.write(key + ": " + value + "\r\n")

f.close()