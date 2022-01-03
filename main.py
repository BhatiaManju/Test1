# first program
print('Hello World!')
num1 = int(input("Enter a number: ")) 
num2 = int(input("Enter another number: ")) 
equal = False 
if num1 > num2: 
	greater = num1 
elif num2 > num1: 
	greater = num2 
elif num1 == num2: 
	equal = True 
if equal: 
	print("The numbers are equal.") 
else: 
	print("The greatest number is " + str(greater))
