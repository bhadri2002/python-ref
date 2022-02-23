# math calculator
#function defining part
def banner():
	print("                 _   _               _ ")
	print("                | | | |             | |")
	print(" _ __ ___   __ _| |_| |__   ___ __ _| |")
	print("| '_ ` _ \ / _` | __| '_ \ / __/ _` | |")
	print("| | | | | | (_| | |_| | | | (_| (_| | |")
	print("|_| |_| |_|\__,_|\__|_| |_|\___\__,_|_|")

#end banner
def end():
	print("               ____  _  _  ____                 ")
	print(" ___  ___  ___( ___)( \( )(  _ \  ___  ___  ___ ")
	print("(___)(___)(___))__)  )  (  )(_) )(___)(___)(___)")
	print("              (____)(_)\_)(____/                ")

# sum function     
def sum(a,b):
	print("\n sum of two number:",a+b)

# subraction function
def sub(a,b):
	print("\n subraction of two number:",a-b)

# multiplication function
def mlt(a,b):
	print("\n multiplication of two number:",a*b)

# division function
def div(a=80,b=10):
	print("\n division of two number:",a/b)


#function calling part
import sys
argv=sys.argv

if(len(argv) > 1):
	banner()
	print()
else:
	print('need argument')
	sys.exit()

#a=int(input("Enter the value for A:"))
#b=int(input("Enter the value for B:"))
#print()
#end()