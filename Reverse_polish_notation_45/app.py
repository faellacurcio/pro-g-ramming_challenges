expression = str(input("Insert expression:"))

expression =  expression.split(" ")

result = 0


def debug_print(string):
	print("")
	print(string)
	print("")

while len(expression) > 1:

	plusIndex = 999
	minusIndex = 999
	timesIndex = 999
	divIndex = 999

	try:
		print(expression)

		if("+" in expression):
			plusIndex = expression.index("+")
		if("-" in expression):
			minusIndex = expression.index("-")
		if("*" in expression):
			timesIndex = expression.index("*")
		if("/" in expression):
			divIndex = expression.index("/")

		debug_print([plusIndex, minusIndex, timesIndex, divIndex])
		
		operation = min(plusIndex, minusIndex, timesIndex, divIndex)
		
		if(operation == plusIndex):
			result = int(expression.pop(operation - 2))+int(expression.pop(operation - 2))
			expression.pop(operation - 2)
			expression.insert(operation - 2,result)
		elif(operation == minusIndex):
			result = int(expression.pop(operation - 2))-int(expression.pop(operation - 2))
			expression.pop(operation - 2)
			expression.insert(operation - 2,result)
		elif(operation == timesIndex):
			result = int(expression.pop(operation - 2))*int(expression.pop(operation - 2))
			expression.pop(operation - 2)
			expression.insert(operation - 2,result)
		elif(operation == divIndex):
			result = int(expression.pop(operation - 2))/int(expression.pop(operation - 2))
			expression.pop(operation - 2)
			expression.insert(operation - 2,result)
		
	except Exception as e:
		print("Bad expression")
		raise e

print("The result is: ",result)