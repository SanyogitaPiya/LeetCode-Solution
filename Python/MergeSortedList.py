class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def mergeTwoLists(list1, list2):
    if list1 == None and list2 == None:
        return None
    if list1 == None and list2 != None:
        return list2
    if list1 != None and list2 == None:
        return list1
    low = list1
    high = list2
    newNode = Node(list1.val)
    ret = newNode
    if list1.val<list2.val :
        low = list1.next
    else:
        newNode.val = list2.val
        low =  list2.next
        high = list1
    while(low and high):
        if(low.val<high.val):
            a = Node(low.val)
            newNode.next = a
            low = low.next
        elif high.val<low.val :
            b = Node(high.val)
            newNode.next = b
            high = high.next
        else:
            c = Node(low.val)
            d = Node(high.val)
            c.next = d
            newNode.next = c
            newNode =newNode.next
            low = low.next
            high = high.next
        newNode = newNode.next
    if(low==None and high!=None):
        while(high!=None):
            e = Node(high.val)
            newNode.next = e
            newNode = newNode.next
            high = high.next
    elif(low!=None and high==None):
        while(low!=None):
            e = Node(low.val)
            newNode.next = e
            newNode = newNode.next
            low = low.next
    while(ret):
        print(ret.val)
        ret = ret.next

# Create the linked list
nodea1 = Node(1)
nodea2 = Node(2)
nodea3 = Node(4)
nodea4 = Node(5)

nodeb1 = Node(3)
#nodeb2 = Node(4)
#nodeb3 = Node(5)
 
nodea1.next = nodea2
nodea2.next = nodea3
nodea3.next = nodea4
#nodeb1.next = nodeb2
#nodeb2.next = nodeb3

mergeTwoLists(nodeb1,nodea1)

