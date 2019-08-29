
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
  def function(self):
    print("This is a message inside the class.")
    print('More')

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
  def lengthOfLongestSubstringOptimized(self, theString):
    n = len(theString)
    answer = i = j = 0
    char_map = {} # char_map[char] = location of last char occurance
    for j in range(n):
      if (theString[j] in char_map):
        i = max(i, char_map[theString[j]])

      answer = max(answer, j-i+1)
      char_map[theString[j]] = j+1
    return answer
  
  #https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/
  def lengthOfLongestSubstringGeeksForGeeks(self, theString):
    n = len(theString) 
    cur_len = 1       # To store the length of current substring 
    max_len = 1       # To store the result 
    prev_index = 0    # To store the previous index 
    i = 0
  
    # Initialize the visited array as -1, -1 is used to indicate 
    # that character has not been visited yet. 
    visited = [-1] * 256
  
    # Mark first character as visited by storing the index of 
    # first character in visited array. 
    visited[ord(theString[0])] = 0
  
    # Start from the second character. First character is already 
    # processed (cur_len and max_len are initialized as 1, and 
    # visited[str[0]] is set 
    for i in range(1, n): 
      prev_index = visited[ord(theString[i])] 
  
      # If the currentt character is not present in the already 
      # processed substring or it is not part of the current NRCS, 
      # then do cur_len++ 
      if prev_index == -1 or (i - cur_len > prev_index): 
        cur_len+= 1
      # If the current character is present in currently considered 
      # NRCS, then update NRCS to start from the next character of 
      # previous instance. 
      else: 
        # Also, when we are changing the NRCS, we should also 
        # check whether length of the previous NRCS was greater 
        # than max_len or not. 
        max_len = max(max_len, cur_len)
        
        cur_len = i - prev_index 
  
      # update the index of current character 
      visited[ord(theString[i])] = i 
  
    # Compare the length of last NRCS with max_len and update 
    # max_len if needed 
    if cur_len > max_len: 
        max_len = cur_len 
  
    return max_len     

  #https://www.geeksforgeeks.org/print-longest-substring-without-repeating-characters/
  def findLongestSubstring(self, theString): 
    n = len(theString)  
    # starting point of current substring.  
    st = 0
    # maximum length substring without  
    # repeating characters.  
    maxlen = 0
    # starting index of maximum  
    # length substring.  
    start = 0
    # Hash Map to store last occurrence  
    # of each already visited character.  
    pos = {}  
    # Last occurrence of first 
    # character is index 0  
    pos[theString[0]] = 0
  
    for i in range(1, n):  
      # If this character is not present in hash,  
      # then this is first occurrence of this  
      # character, store this in hash.  
      if theString[i] not in pos:  
        pos[theString[i]] = i  
  
      else: 
        # If this character is present in hash then  
        # this character has previous occurrence,  
        # check if that occurrence is before or after  
        # starting point of current substring.  
        if pos[theString[i]] >= st:  
          # find length of current substring and  
          # update maxlen and start accordingly.  
          currlen = i - st  
          if maxlen < currlen:  
            maxlen = currlen  
            start = st  
  
            # Next substring will start after the last  
            # occurrence of current character to avoid  
            # its repetition.  
          st = pos[theString[i]] + 1
        # Update last occurrence of  
        # current character.  
        pos[theString[i]] = i  
          
    # Compare length of last substring with maxlen  
    # and update maxlen and start accordingly.  
    if maxlen < i - st:  
      maxlen = i - st  
      start = st  
      
    # The required longest substring without  
    # repeating characters is from string[start]  
    # to string[start+maxlen-1].  
    return theString[start : start + maxlen]  


#print(Solution().lengthOfLongestSubstringNaive('ababcd'))
#print(Solution().lengthOfLongestSubstringBasic('abcdcdefghijklmndxyz'))
#print(Solution().lengthOfLongestSubstringOptimized('abcdcdefghijklmndxyz'))
print(Solution().findLongestSubstring('abcdcdefghijklmndxyz'))
print('end')


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

