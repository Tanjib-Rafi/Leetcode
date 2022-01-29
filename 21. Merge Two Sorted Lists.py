# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        p1,p2 = list1,list2
        
        dummy = ListNode()
        temp  = dummy  
        '''
           Everything is considered an object in python.We we did temp = dummy,
           that means we stored the reference(pointer) for dummy variable into temp.
           Now everytime the temp variable is changed it would also affect the dummy variable
        '''
        
        
        while p1 and p2 :
          
            if p1.val < p2.val :
                temp.next = p1
                p1 = p1.next
                
            else :
                temp.next = p2
                p2 = p2.next
            
            
            temp = temp.next
            
            
        if p1 :
            temp.next = p1
        if p2 :
            temp.next = p2
          
        return dummy.next
      
      

'''
When the head of the Linked List doesn't contain any Nodes at all,
you create a Dummy Head (Node) pointed from that head.
So that you would always be able to reach e.g. head.val or head.next without doing any extra checks.
That's why we are returning dummy.next.
'''
