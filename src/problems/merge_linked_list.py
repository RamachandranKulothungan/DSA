# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = None
        temp1 = list1
        temp2 = list2
        prev = None
        while temp1 or temp2:
            if not temp1:
                curr = temp2
                temp2 = temp2.next
            elif not temp2:
                curr = temp1
                temp1 = temp1.next
            else:
                if temp1.val < temp2.val:
                    curr = temp1
                    temp1 = temp1.next
                else:
                    curr = temp2
                    temp2 = temp2.next
            if not head:
                head = curr
            if prev:
                prev.next = curr
            prev = curr
        return head
        