class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
def hasCycle(head):
    if head== None or head.next==None:
        return False
    #Fast and Slow pointer
    if head== None or head.next==None:
            return False
    slow = head
    fast = head
    while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                return True
            
    return False

node1 = Node(-1)
node2 = Node(-7)
node3 = Node(7)
node4 = Node(-4)
node5 = Node(19)
node6 = Node(6)
node7 = Node(-9)
node8 = Node(-5)
node9 = Node(-2)
node10 = Node(-5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10
node10.next = node10

print(hasCycle(node1))