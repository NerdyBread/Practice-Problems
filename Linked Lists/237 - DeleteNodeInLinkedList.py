class ListNode:
    def __init__(self, next, val):
        self.next = next
        self.val = val

def deleteNode(self, node):
	node.val = node.next.val # Take value from next node
	node.next = node.next.next # Skip next node which had its value taken