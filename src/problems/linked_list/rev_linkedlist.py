from problems.linked_list.linked_list_helper import ListNode


class Solution:
    def reverseList(self, head):
        if not head:
            return []
        tail = head
        while tail.next:
            temp = tail.next.next
            tail.next.next = head
            head = tail.next
            tail.next = temp
        return head


head = ListNode().create_list(range(10))

ListNode().print_linked_list(head)

ListNode().print_linked_list(Solution().reverseList(head))
