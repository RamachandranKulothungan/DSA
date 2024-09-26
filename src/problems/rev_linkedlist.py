# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if not head:
            return []
        temp = head
        tail = head
        while temp:
            c = temp.next
            temp.next = head
            head = temp
            temp = c
        tail.next = None
        return head
    
    def print_linked_list(self, head):
        temp = head
        count = 0
        while temp and count < 12:
            print(temp.val, end=",")
            temp = temp.next
            count+=1
        print("\n")

head = None
tail = None
for n in range(10):
    Node = ListNode(n)
    if not head:
        head = Node
    if not tail:
        tail = Node
        continue
    tail.next = Node
    tail = Node

Solution().print_linked_list(head)

Solution().print_linked_list(Solution().reverseList(head))