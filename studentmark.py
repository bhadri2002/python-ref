# student mark and per store

import os
import sys
from colorama import Fore

db=[]

#clear function
def cls():
	os.system('clear')

#data collect function
def datacollect():
	name = input("Enter student name:")
	mark1 = int(input("Enter mark1:"))
	mark2 = int(input("Enter mark2:"))
	mark3 = int(input("Enter mark3:"))
	per = (mark1+mark2+mark3)/3
	endata = {"name":name,"marks":[mark1,mark2,mark3],"parcent":per}
	db.append(endata)
	cls()
	print()
	print("data stored successfully".center(100,'*'))
	return endata

#show value function
def showvalue():
	dd='-'
	data=['Student Name','Total Marks','Percentage']
	print(dd*100)
	for i in range(len(data)):
		print(data[i].center(30,' '),end=" ")
	print()
	print(dd*100)
	for i in range(len(db)):
		key = list(db[i].keys())
		for j in range(len(key)):
			# print(db[i][key[j]].center(30," "),end=" ")
			if key[j] == "parcent":
				pr=str("%0.2f"%db[i][key[j]])+' %'
				print(pr.center(30," "),end=" ")
			elif key[j] == "marks":
				marks = db[i][key[j]]
				count=0
				for k in range(len(marks)):
					count+=marks[k]
				print(str(count).center(30," "),end=" ")
			else:
				print(str(db[i][key[j]]).center(30," "),end=" ")
		print()
		print(dd*100)

# show message function
def message():
	print('''[1]new student data
[2]view student data
[0]exit
''')

# option choose function
def choose():
	while True:
		try:
			choose = int(input("choose option $ "))
			return choose
		except:
			print("kannaaaa thooranthuuu paaruu.......ena option irukunu.")


while(1):
	message()
	val = choose()
	if(val == 1):
		datacollect()
	elif(val == 2):
		cls()
		showvalue()
	elif(val == 0):
		print('poiitu vaaran brooo.....')
		sys.exit()
	else:
		print('option la ilalaiheyyyyy.....')
		print()