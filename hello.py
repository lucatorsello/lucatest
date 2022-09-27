import sys
def hello():
	if sys.argv[1] == "mars":
		hellomars()
	else:
		helloworld()
def hellomars():
	print("Hello mars")
def helloworld():
	print("Helo World")
if __name__ == '__main__' :
	hello()

