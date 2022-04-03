# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currentl2=l2
        currentl1=l1
        n1=''
        n2=''
        while currentl2!=None and currentl1!=None:
            
            n2+=str(currentl2.val)
            
            currentl2=currentl2.next
        while currentl1!=None:
            n1+=str(currentl1.val)
            currentl1=currentl1.next
            
            
        s=str(int(n1[::-1])+int(n2[::-1]))
        prev=ListNode()
        for i in range(len(s)):
            if(i == len(s)-1):
                prev.val=s[i]
            else:
                temp=ListNode()
                temp.val=s[i]
                temp.next=prev.next
                prev.next=temp
        return prev
        