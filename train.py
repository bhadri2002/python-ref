import sys

argv = sys.argv

if(len(argv) > 1):
	print("Argument here")
	print(argv[1:])
else:
	print("plese enter the argument")
	sys.exit(1)