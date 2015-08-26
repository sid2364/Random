"""
This is a program in Python to mimic a simplex reflex agent
for a vacuum cleaner's environment.

All initial dirt configurations can be achieved
as dirt is a randomly generated environment variable.

The setting of this simulation is in a universe of
4 locations, or tiles, between which the vacuum cleaning bot 
can move.

Performance scores are given based on whether cleaning is
required, the bot has to move or is in the same location, etc.
"""
import random, time
global currPlace
def sense(place):
	global currPlace, score, dirtConfig
	r=random.randrange(0, 10, 1)
	state = {"Dirty":1, "Clean":2}
	#probability of being dirty isnt 0.5
	#something like 3/10 (?)
	if r > dirtConfig:		
		print ("Location "+ str(place) +" is dirty.")
		print ("Cleaning required!")
		score=score-1.0
		if currPlace != place:
			goto(place)
		else:
			print("Bot present at the same location.")
			score=score+3.0
		#move to the place
		return state["Dirty"]
	else:
		print ("Location "+str(place)+" is clean.")
		score=score+1.0
		return state["Clean"]
def clean():
	global currPlace, score
	place = [0, 1, 2, 3]
	for p in place:
		#iteratively check each location
		if sense(p) == 1:
			print ("Location " + str(p) + " has been cleaned!")
		print("Current location is "+ str(currPlace)+"\n")
		time.sleep(3)
def goto(place):
	global currPlace, score
	#move vaccuum to the place we want
	print("Moving  from "+str(currPlace)+" to location "+str(place))
	score=score-1.5
	currPlace=place
global currPlace, score, dirtConfig
score=5
print("\n\t\tVaccuum Cleaner Agent Function Simulation!")
#based on judgement that this function performs decently well
position={"top left":0, "top right":1, "bottom left":2, "bottom right":3}
posyn=input("Do you wish to place the vaccuum cleaner at a particular position? Y/N: ")
if posyn.lower() == "y":
	print("Choose from the following:-\nTop Left, Top Right, Bottom Left, Bottom Right.")
	try:
		pos=input("Enter here: ")
		currPlace=position[pos.lower()]
	except KeyError:
		print("Choice not understood. Starting at random position.")
		currPlace=random.randrange(0, 3, 1)
else:
	currPlace=random.randrange(0, 3, 1)
num=0
scoreadd=[]
print("Vaccuum has been placed at position "+str(currPlace))
print("How dirty would you describe the environment to be?")
dirt={"extremely dirty":4, "dirty":5, "clean":6, "quite clean":7}
d=input("Extremely Dirty, Dirty, Clean, Quite Clean: ")
try:
	dirtConfig=dirt[d.lower()]
	print ("Simulation will be for an environment that is %s." % d)
except KeyError:
		print("Choice not understood. Assuming environment to be clean.")
		dirtConfig=6
try:
	n=input("Input the number of iterations you wish to monitor: ")
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
print("\nThe average performance rating for this simulation is "+str(average))
input("\nEnter any key to continue...")
