# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        t = head
        count = 0
        while t:
            count = count + 1
            t = t.next

        index_left = count - n
        print("count", count)
        print("index_left", index_left)
        if index_left == 0:
            head = head.next
        else:
            t = head
            prev = None
            i = 0
            while i < count:
                if i == index_left:
                    prev.next = t.next
                    break
                prev = t
                t = t.next
                i = i + 1
        return head
