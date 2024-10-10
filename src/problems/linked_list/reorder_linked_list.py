from problems.linked_list.linked_list_helper import ListNode


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # n^2
        # t = head
        # while t:
        #     # self.print_linked_list(head)
        #     t_2 = t.next
        #     if t_2 and t_2.next:
        #         while t_2.next:
        #             t_3 = t_2
        #             t_2 = t_2.next
        #         t_3.next = None
        #         t_4 = t.next
        #         t.next = t_2
        #         t_2.next = t_4
        #     t = t.next.next if t.next else None
        #     # self.print_linked_list(head)
        #     # print(t if not t else t.val)
        # ListNode().print_linked_list(head)

        # SPLIT THE LIST TO HALF AND THEN REVERSE THE SECOND PART AND THEN MERGE THE LINKED LISTS
        # O(n)
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        # print(slow.val)
        slow.next = None
        # ListNode().print_linked_list(head)
        # ListNode().print_linked_list(head2)
        head2 = ListNode().reverseList(head2)
        # ListNode().print_linked_list(head2)

        t1 = head
        t2 = head2
        while t1 and t2:
            temp = t1.next
            t1.next = t2
            temp2 = t2.next
            t2.next = temp
            t2 = temp2
            t1 = temp
        ListNode().print_linked_list(head)


a = [1, 2, 3, 4, 5]
head = ListNode().create_list(a)

Solution().reorderList(head)
