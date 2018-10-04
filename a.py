import re
import csv
import os


def isZ(sss):
	DX = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	return sss[0] in DX

def isDate(sss):
	if sss[-1] in [".", ","]:
		sss = sss[:-1]
	week = ["week", "Wednesday", "Tuesday", "Sunday", "Monday", "Thursday", "Friday", "Saturday"]
	month = ["month", "April"]
	return sss in week or sss in month

def isP(sss):
	prep = ["in", "on", "at", "by", "from", "over", "across", "without", "through", "with", "of", "for", "since", "as"]
	return sss in prep

def isV(sss):
	verb = ["claims", "became", "overtook", "rose", "left", "won", "made", "was", "were", "had", "have", "been"]
	return sss in verb
	
def isThe(sss):
	the = ["the", "The"]
	return sss in the

def isAn(sss):
	an = ["A", "a", "an", "An"]
	return sss in an

def isConj(sss):
	conj = ["while", "when", "after"]
	return sss in conj
	
def isAnd(sss):
	And = ["and"]
	return sss in And
	
def isTo(sss):
	to = ["to"]
	return sss in to

def isNum(sss):
	num = "0123456789"
	if sss[0] in num:
		return True
	num = ["two", "four"]	
	return sss in num
	
def isEd(sss):
	if sss in ["red"]:
		return False
	return re.match(r"\w+ed$", sss)

def isIng(sss):
	return re.match(r"\w+ing$", sss)
	
def isN(i, l, lv):
	if lv[i+1] in ["."]:
		return True
		
	#if (i > 0) and (lv[i-1] in ["the", "an", "p"]):
	#	return True
	
	if (lv[i+1] in ["p", "conj", "to", "v", "and", "ed"]):
		return True
	
	return False


def isToV(i, l, lv):
		
	if (i > 0) and (lv[i-1] in ["to"]):
		return True
	
	return False

def isIngV(i, l, lv):
		
	if (i > 0) and (l[i-1] in ["after", "still"]):
		return True

	if (i > 0) and (l[i-1][-1] in [","]):
		return True	
		
	return False
		
def printList(l, lv, li):
	for i in range(len(l)):
		print(l[i] + "," + str(i) + "," + lv[i] + "," + str(li[i]))

def findNSB(l, lv, li):
	lastIndex = -1
	for i in range(len(l)-1):
		if l[i] in [","]:
			if lastIndex == -1:
				if lv[i+1] in ["v"]:
					continue
				lastIndex = i
			else:
				curIndex = i
				
				for j in range(lastIndex, curIndex + 1):
					li[j] = 99
				return
		
def findPrevN(l, lv, li, ii):
	lastIndex = -1
	for i in range(ii - 1, 0, -1):
		if li[i] > 90:
			continue
		if li[i] > 0:
			break
		if lv[i] in ["n", "Z"]:
			if lastIndex == -1:
				lastIndex = i
		if lv[i] in ["p"]:
			lastIndex = -1
		if lv[i] in ["conj", ".", "and"]:
			break
	return lastIndex

def findNextN(l, lv, li, ii):

	lastIndex = -1
	for i in range(ii + 1, len(l)):
		if li[i] > 90:
			continue
		if li[i] > 0:
			break
		if lv[i] in ["n", "Z"]:
			lastIndex = i
		if lv[i] in ["p", "and", "conj", "ed", "v"]:
			break

	return lastIndex
			
def setLevel(l, lv, li):

	# level 1
	level = 1
	for i in range(len(l)):
		if li[i] > 0:
			continue
		if isSymbol(l[i]):
			li[i] = 1
			continue
		if lv[i] in ["ed", "v"]:
			print(">>>>>>>>>en, v")
			print(l[i])
			li[i] = 1
			m = findPrevN(l, lv, li, i)
			if m > -1:
				li[m] = 2
				print(l[m])
			m = findNextN(l, lv, li, i)
			if m > -1:
				li[m] = 2
				print(l[m])
		elif lv[i] in ["conj", "and"]:
			li[i] = 1
					
def printSkeleton(l, lv, li, level):
	ll = []
	
	# level 1
	for i in range(len(l)):
		if li[i] < 1:
			continue
		if li[i] > level:
			continue
		else:
			lll = [l[i], i, lv[i]]
			ll.append(lll)
			li[i] = 1
	
	for j in range(len(ll)):
		print(ll[j][0] + "," + str(ll[j][1]) + "," +ll[j][2])

def isSymbol(ss):
	return ss in [",", "."]
	
def cleanData(l):
	# extract , .
	for i in range(len(l)-1, -1, -1):
		if isSymbol(l[i][-1]):
			l.insert(i+1, l[i][-1])
			l[i] = l[i][:-1]

	# combine "at least"..
	wl = ["at least", "more than"]
	for i in range(len(l)-2, -1, -1):
		if (l[i] + " " + l[i+1]) in wl:
			l[i] = l[i] + " " + l[i+1]
			l.pop(i+1)
	
def splitSentence(s):

	l = s.split()

	cleanData(l)
			
	lv = []

	i = 0

	# first scan
	for ss in l:
		if isDate(ss):
			lv.append("D")
		elif isSymbol(ss):
			lv.append(ss)
		elif isAnd(ss):
			lv.append("and")
		elif isNum(ss):
			lv.append("9")
		elif isTo(ss):
			lv.append("to")
		elif isThe(ss):
			lv.append("the")
		elif isAn(ss):
			lv.append("an")
		elif isZ(ss):
			lv.append("Z")
		elif isP(ss):
			lv.append("p")
		elif isV(ss):
			lv.append("v")
		elif isEd(ss):
			lv.append("ed")
		elif isIng(ss):
			lv.append("ing")
		elif isConj(ss):
			lv.append("conj")
		else:
			lv.append("")

	# scan for v
	for i in range(len(l)):
		if lv[i] == "ing":
			if isIngV(i, l, lv):
				lv[i] = "v"
			else:
				lv[i] = ""

		if len(lv[i]) != 0:
			continue
		
		if isToV(i, l, lv):
			lv[i] = "v"
			
	# scan for n
	for i in range(len(l)):
		if len(lv[i]) != 0:
			continue
		
		if isN(i, l, lv):
			lv[i] = "n"
	
	return l, lv

def splitEng(fname):
	f = open(fname, "r")

	title = []
	sentence = []

	index = 0
	for line in f:
		index += 1
		if index == 4:
			index = 0
		if index == 2 or index == 0:
			continue
		s = line[:-1]
		if index == 1:
			title.append(s)
		else:
			sentence.append(s)
		
	f.close()
	
	return title, sentence

def outputTitle(fname, title, sentence):

	with open(fname, 'w') as csvfile:
		fieldnames = ['No', 'title', 'sentence']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator="\n")

		writer.writeheader()	
		for i in range(len(title)):
			writer.writerow({fieldnames[0]: i + 1, fieldnames[1] : title[i], fieldnames[2] : sentence[i]})
    	
	csvfile.close()	

def outputDetail(fname, no, l, lv):

	with open(fname, 'a') as csvfile:
		fieldnames = ['No', 'word', 'v']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator="\n")
		
		if no == 1:
			writer.writeheader()	
			
		for i in range(len(l)):
			writer.writerow({fieldnames[0]: no, fieldnames[1] : l[i], fieldnames[2] : lv[i]})
    	
	csvfile.close()		
		
########
s = "U.S. President Donald Trump and Japanese Prime Minister Shinzo Abe agreed on Wednesday to start negotiation on a bilateral trade agreement on goods."

#s = "US actor Will Smith celebrated his 50th birthday by bungee jumping from a helicopter over the Grand Canyon while his family and friends watched."

#s = "37-year-old South Korean Yang Yong-Eun became the first Asian male to win a major championship when he overtook Tiger Woods to clinch the U.S. PGA title on Sunday."

#s = "17-year-old Ryo Ishikawa, the youngest player to compete in a PGA Championship, made his first cut at a major tournament on Friday, after missing the cut at the Masters in April and the British Open last month."

s = "Four people were killed and more than 200 were injured after powerful typhoon Trami ripped through Japan over the weekend. The destructive storm caused widespread traffic disruption and left more than 750,000 homes without power across the country."

s = "A large-scale earthquake with a magnitude of 6.5 rocked Shizuoka Prefecture in central Japan early Tuesday, injuring at least 100 people."

s = "A Chinese bride attempted to establish a new Guinness world record for the longest wedding dress, walking down the aisle in a gown with a 7,083 feet (2,162m) long train and 9,999 red silk roses, the Xinhua News Agency reported."

s = "Mark Lester, a British former child star and long-time friend of Michael Jackson, claims to be the biological father of the late pop star's daughter Paris, a London-based tabloid newspaper reported."


fname = "C:/Users/tnd.sour/Desktop/sou/eng/eng.txt"

title, sentence = splitEng(fname)

fname = "C:/Users/tnd.sour/Desktop/sou/eng/t-s.csv"
outputTitle(fname, title, sentence)




fname = "C:/Users/tnd.sour/Desktop/sou/eng/w-v.csv"
try:
	os.remove(fname)
except:
	pass
	
for i in range(len(sentence)):
	
	l, lv = splitSentence(sentence[i])
	outputDetail(fname, i+1, l, lv)



li = []

for i in range(len(l)):
	li.append(0)
	
#get noun-sub-block
findNSB(l, lv, li)

setLevel(l, lv, li)
		
# output list
printList(l, lv, li)

print(">>>>>>>>1")
printSkeleton(l, lv, li, 1)

print(">>>>>>>>2")
printSkeleton(l, lv, li, 2)

