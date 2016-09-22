#########################################################
##  CS 4750 (Fall 2016), Assignment #1, Question #3    ##
##   Script File Name: index1.py                       ##
##       Student Name: Adam Smith                      ##
##         Login Name: aes702                          ##
##              MUN #: 201036597                       ##
#########################################################

import sys
import string
import collections

#########################
## loadIgnoreList(fileName)
## Input: fileName: path to file.
## return: return set of words from specified file
#########################
def loadIgnoreList(fileName):
	#open file
	f = open(fileName, "r")
	#initalize set
	words = set()

	#read each word in file
	for line in f:
		for word in line.split():
			#add word to set
			print word
			words.add(word)

	#close file
	f.close()

	#return set
	return words

#########################
## getLineNumbers(ignored, fileName)
## Input: ignored: set containing words to ignore
## fileName: path to file to generate line numbers from
## return: disctionary with word => line numbers
#########################
def getLineNumbers(ignored, fileName):
	lines = {}
	#open file for reading
	f = open(fileName, "r")

	#keep track of line number
	lineNumber = 1
	#iterate through lines
	for line in f:
		#split each word in line
		for word in line.split():
			#remove punctuation
			word = word.translate(None, string.punctuation)
			#check valid word length
			if not len(word) > 0:
				continue
			#check if word is not in ignored list
			if not word in ignored:
				#append lineNumber to value of list[word]
				if not lines.has_key(word):
					lines[word] = str(lineNumber) + " "
				else:
					lines[word] += str(lineNumber) + " "
		#increment line number
		lineNumber += 1

	#return lines
	return lines

#ignored path
ignored = sys.argv[1]
#text path
text = sys.argv[2]
#output path
output = sys.argv[3]

#generate line numbers
lines = getLineNumbers(loadIgnoreList(ignored), text)
#sort the array by key
sortedLines = collections.OrderedDict(sorted(lines.items()))

#open to write
f = open(output, "w")

#write key: lineNumbers
for key, value in sortedLines.items():
	f.write(key + ": " + value + "\n")

#close the file!
f.close()
