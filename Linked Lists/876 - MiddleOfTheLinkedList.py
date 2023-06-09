class ListNode:
	def __init__(self, next, val):
		self.next = next
		self.val = val

def middleNode(self, head: ListNode) -> ListNode:
	slow = fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	return slow