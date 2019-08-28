
# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, data):
    self.val = data
    self.next = None
class LinkedList: 
  # Function to initialize head 
  def __init__(self): 
    self.head = None
  # Function to reverse the linked list 
  def reverse(self): 
    prev = None
    current = self.head 
    while(current is not None): 
      next = current.next
      current.next = prev 
      prev = current 
      current = next
    self.head = prev 
  # Function to insert a new node at the beginning 
  def push(self, new_data): 
    new_node = ListNode(new_data) 
    new_node.next = self.head 
    self.head = new_node 
  # Utility function to print the linked LinkedList 
  def printList(self): 
    temp = self.head 
    while(temp): 
      print(temp.data) 
      temp = temp.next

class Solution:
  variable = "Solution"
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
  def reverse(self,list):
    current = list
    builder = None
    rev = None
    while (current != None):
      builder = ListNode(current.val)
      builder.next = rev
      rev = builder
      current = current.next
    return rev    
  def push(self, l ,new_data): 
    newNode = ListNode(new_data)
    newNode.next =  l
    return newNode
  def addTwoNumbers(self, list1, list2):
    sum = rem = num1 = num2 = 0
    sumNodes = newSumNode = lastNode = None
    val1 = list1
    val2 = list2

    while (val1 != None or val2 != None):
      if val1 == None: num1 = 0
      else: num1 = val1.val
      
      if val2 == None: num2 = 0
      else: num2 = val2.val

      sum = rem + num1 + num2
      rem = sum // 10
      sum = sum - (rem * 10)
      newSumNode = ListNode(sum)
      
      if sumNodes == None:
        sumNodes = newSumNode
        lastNode = sumNodes
      else:
        lastNode.next = newSumNode
        lastNode = lastNode.next
        
      val1 = val1.next if val1 else None 
      val2 = val2.next if val2 else None 

    
    if rem != 0:
      newSumNode = ListNode(rem)
      lastNode.next = newSumNode
      lastNode = lastNode.next
    
    return sumNodes
  def allUnique(self, s,  start, end):
    pos_set = set()
    ss = s[start:end]
    for i in range(start, end):
      ch = s[i]
      if ch in pos_set: return False
      pos_set.add(ch)
    
    return True
  def lengthOfLongestSubstringNaive(self, s):
    n = len(s)
    ans = 0
    for i in range(n):
      for j in range(i+1, n+1):
        ss = s[i:j]
        if self.allUnique(s, i, j):
          ans = max(ans, j-i)
    
    return ans

  
  def lengthOfLongestSubstringBasic(self, theString):
    n = len(theString)
    pos_set = set()
    answer = i = j = 0
    while (i < n and j < n):
      #try to extend the range [i, j]
      if (theString[j] not in pos_set):
        pos_set.add(theString[j])
        j += 1
        answer = max(answer, j - i)
        
      else:
        pos_set.remove(theString[i])
        i += 1
    return answer

  def lengthOfLongestSubstring(self, theString):
    n = len(theString)
    current_pos = 0
    maxlen = 0
    start = 0
    
    pos ={} 

    pos[theString[0]] = 0

    print(pos)

    for i in range(1,n):
      if theString[i] not in pos:
        pos[theString[i]]=i
      else:
        if pos[theString[i]] >= current_pos:
          current_length = i - current_pos
          if maxlen < current_length:
            maxlen = current_length
            start = current_pos 

          current_pos = pos[theString[i]] + 1
    if maxlen < i - current_pos:
      maxlen = i - current_pos
      start = current_pos
    print(i)
    return theString[start : start + maxlen]  
  

  

#print(Solution().lengthOfLongestSubstringNaive('ababcd'))
print(Solution().lengthOfLongestSubstringBasic('abcdabcdefghijklmnde'))

number = 1
number += 1


#l1 = ListNode(9)
#l1.next = ListNode(9)
##l1.next.next = ListNode(9)

#l2 = ListNode(9)
#l2.next = ListNode(9)
#l2.next.next = ListNode(9)
#Solution().printList(l1)
#print("---------------------")
#Solution().printList(l2)
#print("---------------------")
#result = Solution().addTwoNumbers(l1, l2)
#Solution().printList(result)
#input('Press ENTER to continue...')
# d = ListNode('CC')
# d = Solution().push(d,'BB')
# d = Solution().push(d,'AA')
# d = Solution().push(d,'A0')
# Solution().printList(d)
# Solution().print_backward(d)
# print("---------------------")
# e = Solution().reverse(d)
# Solution().printList(e)

