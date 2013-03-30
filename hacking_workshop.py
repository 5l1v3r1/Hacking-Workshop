#!/usr/bin/env python
#Author: MaYaSeVeN
import random, time, urllib2, json

#candidates = [line.strip() for line in open("candidates.txt", 'r')]

print "\n!!! All of Candidates for Hacking Workshop 6-7 April 2013 !!!\n"

candidatesFromFacebook = ["https://graph.facebook.com/459003187504945/likes?limit=1000&offset=0", "https://graph.facebook.com/150687625092061/likes?limit=1000&offset=0"]
candidates = []

for candidatesFromPost in candidatesFromFacebook:
	candidatesJson = json.load(urllib2.urlopen(candidatesFromPost))
	for candidatesNumber in range(len(candidatesJson["data"])):
		nameOfCandidate = candidatesJson["data"][candidatesNumber]["name"]
		candidates.append(nameOfCandidate)

for candidate in candidates:		
	print "[-]", candidate
	time.sleep(0.1)
print "\nThe number of candidates = ", len(set(candidates))
print "\nTrying to choose the winners\n"

time.sleep(7)
print "Congratulation to [+]", random.choice(candidates), "\n"
