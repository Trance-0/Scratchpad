# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        n=1
        p=head
        while p.next:
            p=p.next
            n+=1
        p.next=head
        k=k%n
        for i in range(n-k):
            p=p.next
        head=p.next
        p.next=None
        return head