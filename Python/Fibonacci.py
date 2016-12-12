#Clinton Tak
#Simple fibonacci sequence with dynamic programming that 
#stores the numbers in a list so known numbers don't have 
#to be recalculated
list1 = [] #List to store numbers 
list1.insert(0, 0) #sets up first and second numbers
list1.insert(1, 1)

def fibonacci(n):
	if (len(list1)<n+1):
		list1.insert(n,fibonacci(n-1) + fibonacci(n-2))
	return list1[n] 
	
print (fibonacci(10))		