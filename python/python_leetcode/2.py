# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = int("".join(map(str, l1))) 
        result2 = int("".join(map(str, l2))) 
        reversed_num2 = int(str(result2)[::-1])
        reversed_num = int(str(result)[::-1])
        print(reversed_num2+reversed_num)
            
               
        
        
        
        
sl=Solution()
sl.addTwoNumbers([2,4,3],[5,6,4])