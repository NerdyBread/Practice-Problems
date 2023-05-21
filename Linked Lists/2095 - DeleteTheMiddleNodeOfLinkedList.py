class ListNode:
	def __init__(self, next, val):
		self.next = next
		self.val = val

def deleteMiddle(self, head: ListNode) -> ListNode:
	middleNode = self._findMiddle(head)
	pointer = head
	if not pointer.next:
		return None
	while pointer.next != middleNode:
		pointer = pointer.next
	pointer.next = middleNode.next
	return head

def _findMiddle(self, head: ListNode) -> ListNode:
	slow = fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	return slow