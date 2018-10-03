import re



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
	prep = ["in", "on", "at", "by", "from", "over", "across", "without", "through", "with", "of", "for"]
	return sss in prep

def isV(sss):
	verb = ["became", "overtook", "left", "made", "were", "had", "have", "been"]
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
		
	if (i > 0) and (l[i-1] in ["after"]):
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
			if lv[i+1] in ["v"]:
				continue
			if lastIndex == -1:
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
	
		
########
s = "U.S. President Donald Trump and Japanese Prime Minister Shinzo Abe agreed on Wednesday to start negotiation on a bilateral trade agreement on goods."

#s = "US actor Will Smith celebrated his 50th birthday by bungee jumping from a helicopter over the Grand Canyon while his family and friends watched."

#s = "37-year-old South Korean Yang Yong-Eun became the first Asian male to win a major championship when he overtook Tiger Woods to clinch the U.S. PGA title on Sunday."

#s = "17-year-old Ryo Ishikawa, the youngest player to compete in a PGA Championship, made his first cut at a major tournament on Friday, after missing the cut at the Masters in April and the British Open last month."

s = "Four people were killed and more than 200 were injured after powerful typhoon Trami ripped through Japan over the weekend. The destructive storm caused widespread traffic disruption and left more than 750,000 homes without power across the country."

s = "A large-scale earthquake with a magnitude of 6.5 rocked Shizuoka Prefecture in central Japan early Tuesday, injuring at least 100 people."

s = "A Chinese bride attempted to establish a new Guinness world record for the longest wedding dress, walking down the aisle in a gown with a 7,083 feet (2,162m) long train and 9,999 red silk roses, the Xinhua News Agency reported."

l = s.split()

cleanData(l)

li = []

for i in range(len(l)):
	li.append(0)
		
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

	
#get noun-sub-block
findNSB(l, lv, li)

setLevel(l, lv, li)
		
# output list
printList(l, lv, li)

print(">>>>>>>>1")
printSkeleton(l, lv, li, 1)

print(">>>>>>>>2")
printSkeleton(l, lv, li, 2)

