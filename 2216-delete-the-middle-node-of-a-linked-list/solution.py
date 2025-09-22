# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list = []
        node = head

        while node:
            print(node.val)
            list.append(node)
            node = node.next

        if len(list) == 1:
            return None
        if len(list) == 2:
            head.next = None
            return head

        i = len(list)//2
        
        list[i-1].next = list[i+1]

        return head
