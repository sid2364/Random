"""
This is a program in Python to mimic a simple reflex agent
for a vacuum cleaner's environment.

All initial dirt configurations can be achieved
as dirt is a randomly generated environment variable.
Probability for each block of getting dirty is 0.2.

The setting of this simulation is in a universe of
9 locations, or tiles, between which the vacuum cleaning bot 
can move.

Performance scores are given based on whether cleaning is
required, the bot has to move or is in the same location, etc.

Path cost and search cost is also calculated.
"""
import random, time, os
global currPlace
def print_gridnew(p):
	j=0
	for i in range(0,9):
		if j==0:
			print("-"*13)
		j+=1
		if p!=i:
			print("|  ", end=" ")
		else:
			print("| X", end=" ")
		if j==3:
			j=0
			print("|")
	else:
		print("-"*13)
def sense(place):
	global currPlace, score, dirtConfig, pathcost, searchcost
	r=random.randrange(1, 10, 1)
	state = {"Dirty":1, "Clean":2}
	searchcost=searchcost+1
	if r >= 9:	#dirty with a probability of 0.2	
		print ("Location "+ str(place) +" is dirty.")
		print ("Cleaning required!")
		score=score-1.5
		if currPlace != place:
			goto(place)
			#print_gridnew(place)
		else:
			print("Bot present at the same location.")
			score=score+3.0
		#move to the place
		return state["Dirty"]
	else:
		print ("Location "+str(place)+" is clean.")
		score=score+0.5
		return state["Clean"]
def clean():
	global currPlace, score, pathcost, searchcost
	place = [0, 1, 2, 3, 4, 5, 6, 7, 8]
	for p in place:
		#iteratively check each location
		if sense(p) == 1:
			print ("Location " + str(p) + " has been cleaned!")
		searchcost+=1
		print_gridnew(currPlace)
		print("Current location is "+ str(currPlace))
		print("Path cost is "+str(pathcost))
		time.sleep(2)
	os.system('cls')
def goto(place):
	global currPlace, score, pathcost, searchcost
	nplace=0
	ncurrPlace=0
	flag=0
	#move vaccuum to the place we want
	print("Moving  from "+str(currPlace)+" to location "+str(place))
	score=score-1.0
	if nplace>=6:
		nplace=place-3
		pathcost+=1
		flag=1
	elif nplace<=3:
		nplace=place+3
		pathcost+=1
	if int(currPlace)<=3 and flag==1:
		ncurrPlace=currPlace+3
		pathcost+=1
	if int(currPlace)>=6 and flag==0:
		ncurrPlace=currPlace-3
		pathcost+=1
	pathcost+=abs(int(ncurrPlace)-int(nplace))
	currPlace=place
os.system('cls')
global currPlace, score, dirtConfig, pathcost, searchcost
pathcost=0
searchcost=0
score=5
print("\n\t\tVaccuum Cleaner Agent Function Simulation!")
#based on judgement that this function performs decently well
posyn=input("Do you wish to place the vaccuum cleaner at a particular position? Y/N: ")
if posyn.lower() == "y":
	print("Choose from the following:-\n")
	j=0
	for i in range(0,9):
		if j==0:
			print("-"*13)
		j+=1
		print("| "+str(i), end=" ")
		if j==3:
			j=0
			print("|")
	else:
		print("-"*13)
	try:
		currPlace=input("Enter here: ")
		while(int(currPlace)<0 or int(currPlace)>8):
			currPlace=input("Not valid. Enter a number between 0 and 8: ")
	except KeyError:
		print("Choice not understood. Starting at random position.")
		currPlace=random.randrange(0, 8, 1)
else:
	currPlace=random.randrange(0, 8, 1)
num=0
scoreadd=[]
print("Vaccuum has been placed at position "+str(currPlace))
print_gridnew(int(currPlace))
try:
	n=input("Input the number of iterations you wish to monitor: ")
	while int(n)<=0:
		n=input("Not a valid input. Enter a non-zero positive number: ")
	number=int(n)
	print("Iterating %d times." % number)
except ValueError:
	print("Could not understand. Iterating 3 times.\n")
	n=3
number=int(n)
while num<number:
	score=5.0
	clean()
	num=num+1
	scoreadd.append(score)
	print ("Performance score after this iteration is "+str(score))
average = 0
sum = 0    
for a in scoreadd:
    sum = sum + a
average = sum / len(scoreadd)
print("The average performance rating for this simulation is "+str(average))
print("The total path cost is "+str(pathcost))
print("The search cost is "+str(pathcost))
input("Enter return key to continue...\n")
os.system('cls')