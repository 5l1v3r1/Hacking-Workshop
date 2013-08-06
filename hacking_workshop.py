#!/usr/bin/env python
#Author: MaYaSeVeN
import random, time, urllib2, json

print "\n!!! All of Candidates for Hacking Workshop 17-18 Augest 2013 !!!\n"

accessToken = "[Facebook_Access_Token]" #Censor

posts = ["506599602745303", "503546013050662"]

candidates = []

for postID in posts:
    candidatesLike = []
    candidatesShare = []

    candidatesFromPostLike = "https://graph.facebook.com/" + postID + "/likes?limit=1000&offset=0"
    candidatesLikeJson = json.load(urllib2.urlopen(candidatesFromPostLike))
    for candidatesLikeNumber in range(len(candidatesLikeJson["data"])):
        nameOfCandidateLike = candidatesLikeJson["data"][candidatesLikeNumber]["name"]
        candidatesLike.append(nameOfCandidateLike)

    candidatesFromPostShare = "https://graph.facebook.com/" + postID + "/sharedposts?limit=1000&access_token=" + accessToken
    candidatesShareJson = json.load(urllib2.urlopen(candidatesFromPostShare))
    for candidatesShareNumber in range(len(candidatesShareJson["data"])):
        nameOfCandidateShare = candidatesShareJson["data"][candidatesShareNumber]["from"]["name"]
        candidatesShare.append(nameOfCandidateShare)

    print "PostID = " + postID + " Like = " + str(len(candidatesLike)) + " Share = " + str(len(candidatesShare))
    candidates = candidates + [candidate for candidate in candidatesShare if candidate in candidatesLike]

time.sleep(4)
for candidate2 in candidates:
    print "[-]", candidate2
    time.sleep(0.1)
print "\nThe number of candidates = ", len(candidates)
print "\nTrying to choose the winners\n"

time.sleep(7)
print "Congratulation to [+]", random.choice(candidates), "\n"
