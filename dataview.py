# data store

import os
import sys

db=[]

#clear function
def cls():
	os.system('clear')

#data collect function
def datacollect():
	name = input("Enter your name:")
	dep = input("Enter your departement:")
	goals = input("Enter your Goals:")
	cgpa = input("Enter your CGPA:")
	hobby = input("Enter your hobby:")
	endata = {"name":name,"departement":dep,"goals":goals,"cgpa":cgpa,"hobby":hobby}
	db.append(endata)
	print("data stored successfully".center(100,'*'))
	return endata

#show value function
def showvalue():
	dd='-'
	data=['name','departement','Goals','CGPA','hobby']
	print(dd*100)
	for i in range(len(data)):
		print(data[i].center(20,' '),end=" ")
	print()
	print(dd*100)
	for i in range(len(db)):
		key = list(db[i].keys())
		for j in range(len(key)):
			print(db[i][key[j]].center(20," "),end=" ")
		print()
		print(dd*100)

# show message function
def message():
	print('''[1]create data
[2]view data
[0]exit
''')

# option choose function
def choose():
	choose = int(input("choose number> "))
	return choose


while(1):
	message()
	val = choose()
	if(val == 1):
		datacollect()
	elif(val == 2):
		cls()
		showvalue()
	else:
		print('poiitu vaaran brooo.....')
		sys.exit()