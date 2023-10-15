# A recursive Python3 program to check 
# whether a given number is palindrome or not 

# A function that returns true 
# only if num contains one digit 
def oneDigit(num): 
	
	# comparison operation is faster 
	# than division operation. So 
	# using following instead of 
	# "return num / 10 == 0;" 
	return ((num >= 0) and
			(num < 10)) 

# A recursive function to find 
# out whether num is palindrome 
# or not. Initially, dupNum 
# contains address of a copy of num. 
def isPalUtil(num, dupNum): 
	
	# Base case (needed for recursion 
	# termination): This statement 
	# mainly compares the first digit 
	# with the last digit 
	if oneDigit(num): 
		return (num == (dupNum[0]) % 10) 

	# This is the key line in this 
	# method. Note that all recursive 
	# calls have a separate copy of 
	# num, but they all share same 
	# copy of *dupNum. We divide num 
	# while moving up the recursion tree 
	if not isPalUtil(num //10, dupNum): 
		return False

	# The following statements are 
	# executed when we move up the 
	# recursion call tree 
	dupNum[0] = dupNum[0] //10

	# At this point, if num%10 
	# contains i'th digit from 
	# beginning, then (*dupNum)%10 
	# contains i'th digit from end 
	return (num % 10 == (dupNum[0]) % 10) 

# The main function that uses 
# recursive function isPalUtil() 
# to find out whether num is 
# palindrome or not 
def isPal(num): 
	# If num is negative, 
	# make it positive 
	if (num < 0): 
		num = (-num) 

	# Create a separate copy of 
	# num, so that modifications 
	# made to address dupNum 
	# don't change the input number. 
	dupNum = [num] # *dupNum = num 

	return isPalUtil(num, dupNum) 

# Driver Code 
n = 12321
if isPal(n): 
	print("Yes") 
else: 
	print("No") 

n = 12
if isPal(n) : 
	print("Yes") 
else: 
	print("No") 

n = 88
if isPal(n) : 
	print("Yes") 
else: 
	print("No") 

n = 8999
if isPal(n) : 
	print("Yes") 
else: 
	print("No") 

# This code is contributed by mits 
