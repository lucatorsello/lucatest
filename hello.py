import sys

def hello():
	if sys.argv[1] == "mars":
		hellomars()
	if sys.argv[1] == "jupiter":
		hellojupiter()
	else:
		helloworld()
def hellomars():
	print("Hello mars")

def hellojupiter():
	print("Helo Jupiter")
	
def helloworld():

	print("Helo World")
if __name__ == '__main__' :
	hello()

