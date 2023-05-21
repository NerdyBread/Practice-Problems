class ListNode:
    def __init__(self, next, val):
        self.next = next
        self.val = val

def pairSum(self, head) -> int:
	slow = fast = head # Create both pointers
	prev = None # Create "prev" node for reversing back half of list
	maxSum = int() # Placeholder for return number
	while fast and fast.next: # So fast doesn't go too far and cause an error
		# Get slow pointer to middle of the list and fast pointer to the end
		slow = slow.next
		fast = fast.next.next
	while slow:
		# Reverse the second half of the linked list
		nextNode = slow.next
		slow.next = prev
		prev = slow
		slow = nextNode
		# So now "prev" points to the end of list and "head" points to the start
	while prev:
		# Once prev is None, we've reached the middle of the list
		maxSum = max((prev.val + head.val), maxSum)
		# See if current twin sum is greater than the one we've found so far
		prev = prev.next
		head = head.next
		# Move nodes to the next twin pair
	return maxSum
def pairSumWithStack(self, head) -> int:
	"""Still uses two pointers but also uses a stack
	O(N) space but doesn't modify the input"""
	slow = fast = head
	stack = [] # Technically stacks in python are just lists
	maxSum = int()
	while fast and fast.next: # Same setup as above
		stack.append(slow.val) # Add the first half of the list to stack
		slow = slow.next
		fast = fast.next.next
	while slow:
		num = stack.pop() + slow.val
		maxSum = max(num, maxSum)
		slow = slow.next
	return maxSum