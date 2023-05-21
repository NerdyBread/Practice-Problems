def isValid(self, s: str) -> bool:
	stack = []
	brackets = {'(': ')', '[': ']', '{': '}'}
		
	for char in s:
		if char in brackets.keys():
			stack.append(char)
		else:
			if stack:
				last = stack.pop()
			else:
				return False
			if char != brackets[last]: # Make sure type of brackets match & close in correct order
				return False
				
	return not len(stack) # Return True if stack is empty