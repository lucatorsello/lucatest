import sys

def hello():
	if sys.argv[1] == "Jupiter":
		hellojupiter()
	else:
		helloworld()
def hellojupiter():
	print("Helo Jupiter")
	
def helloworld():

	print("Helo World")
if __name__ == '__main__' :
	hello()

