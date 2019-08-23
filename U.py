# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  variable = "blah"
  def isPalin(self, ll):
    stck = []
    slow = ll

    while (slow != None):
      stck.append(slow.val)
      slow = slow.next

    slow = ll

    while (slow != None):
      if (slow.val == stck[len(stck)-1]):
        stck.pop()
        slow = slow.next
      else:
        return False


    return True

  def mergeTwoLists(self, l1, l2):
    if l1 is None:
      return l2
    elif l2 is None:
      return l1
    elif l1.val < l2.val:
      l1.next = self.mergeTwoLists(l1.next, l2)
      return l1
    else:
      l2.next = self.mergeTwoLists(l1, l2.next)
      return l2

  def mergeTwoListsIterative(self, l1, l2):
    acurrent = None
    aroot = None
    while True:
      if l1 is None:
        aanextNode = l2
      elif l2 is None:
        aanextNode = l1
      elif l1.val < l2.val:
        aanextNode = l1
      else:
        aanextNode = l2

      if aanextNode == l1:
        l1 = l1.next if l1 else None
      if aanextNode == l2:
        l2 = l2.next if l2 else None

      if aanextNode is None:
        break
      if not acurrent:
        acurrent = aanextNode
        aroot = acurrent
      else:
        acurrent.next = aanextNode
      acurrent = aanextNode
    return aroot

  def function(self):
        print("This is a message inside the class.")
  
  def printList(self, dd):
    while dd:
      print(dd.val)
      dd= dd.next

  def print_backward(self,list):
    if list == None: return
    head = list
    tail = list.next
    self.print_backward(tail)
    print(head.val)
    
  def rev(self,list):
    if list == None : 
      return
    else :
      newNode = ListNode(list.val)
      if list.next == None:
        return newNode
      else :
        
        retunr 
    
    if list.next == None : return newNode
    rest = list.next
    tsil = self.rev(list.next)
    rest.next = newNode
    print('s')
    return tsil
    
      


  def reverse(self, l):
    list_first = None
    list_rest_begin = None
    list_rest_end = None
    if (l == None):
      pass
    elif (l.next == None):
      list_rest_begin = ListNode(l.val)
    else:
      list_first = ListNode(l.val)
      list_rest_begin = ListNode(l.next.val)
      list_rest_begin.next = list_first

    return list_rest_begin

  def Make_first_of_l2__first_of_l1(self, l1, l2):
    if l2 == None:
      return
    
    l3 = l2.next
    l2.next = l1
    l1 = l2
    l2 = l3
    print('sdsd')
      
  def push(self, l ,new_data): 
    ph = l
    l = ListNode(new_data) 
    new_node.next =  l
    l = new_node

# myobjectx = Solution()
# myobjectx.variable

a = ListNode(12)
a.next = ListNode(14)
a.next.next = ListNode(16)
# b = ListNode(2)
# b.next = ListNode(4)
# b.next.next = ListNode(6)
# c = Solution().mergeTwoLists(a,b)
d = ListNode(111)
d.next = ListNode(222)
#d.next.next = ListNode(333)
Solution().printList(d)
Solution().print_backward(d)
print("---------------------")
e = Solution().rev(d)
Solution().printList(e)

Solution().printList(d)

#
#e = Solution().reverse(d)
#Solution().printList(d)
#Solution().printList(e)
# print(e.next.val)

# print(d.val)
# print(d.next.val)