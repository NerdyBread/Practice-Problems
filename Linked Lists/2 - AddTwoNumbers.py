class ListNode:
    def __init__(self, next, val):
        self.next = next
        self.val = val

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
	result = ListNode() # Result linked list
	resultPointer = result # Traverse through result
	pointer1 = l1
	pointer2 = l2
	carry = 0 # Carry bit
	while True:
		sum = pointer1.val + pointer2.val + carry
		if sum < 10: 
			# If this we can just add this digit and move on
			resultPointer.val = sum
			carry = 0
		else:
			# If not we carry the ten and add what's left
			resultPointer.val = sum-10
			carry = 1
		# Update pointers
		pointer1 = pointer1.next
		pointer2 = pointer2.next
		if pointer1 == None and pointer2 == None and carry == 0:
			# We're done if we've traversed everything
			return result
		resultPointer.next = ListNode()
		resultPointer = resultPointer.next
		# If not done add to result list and set pointer to new node
		if pointer1 == None:
			pointer1 = resultPointer
			# Stops errors on line 14 if one list is longer than the other
		if pointer2 == None:
			pointer2 = resultPointer