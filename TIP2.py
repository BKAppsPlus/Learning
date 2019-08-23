# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
      self.val = x
      self.next = None

class LinkedList: 
  # Function to initialize head 
  def __init__(self): 
    self.head = None

  # Function to insert a new node at the beginning 
  def push(self, new_data): 
    new_node = Node(new_data) 
    new_node.next = self.head 
    self.head = new_node 


class Solution:
  #def addTwoNumbers(self, l1, l2, c = 0):

    # Fill this in.
  def reverse(self, l):
    list_first = None
    list_rest = None
    if (l == None or l.next == None):
      return l

    list_first = ListNode(l.val)
    list_rest = l.next

    list_rest = self.reverse(list_rest)
    
    list_rest.next = list_first
    list_first.next = None
    
    return list_rest



b = ListNode(2)
b.next = ListNode(4)
b.next.next = ListNode(6)

llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(85) 

a = Solution().reverse(b)
print(a.val)
print(a.next.val)
