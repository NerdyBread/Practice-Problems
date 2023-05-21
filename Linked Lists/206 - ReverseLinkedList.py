class ListNode:
	def __init__(self, next, val):
		self.next = next
		self.val = val
		
def reverseList(self, head: ListNode) -> ListNode:
	prev = None
	while head:
		nextNode = head.next # Save next node before head no longer points to it
		head.next = prev # Switch head reference to previous node
		# Setting up next iteration by moving everything up one
		prev = head
		head = nextNode
	return prev # Head points to None so return prev