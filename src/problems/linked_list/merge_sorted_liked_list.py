# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        temp_list = [lists[x] for x in range(len(lists))]
        head = None
        prev = None
        count_none = 0
        for temp in temp_list:
            if not temp:
                count_none = count_none + 1
        # print("count_none", count_none)

        while count_none < len(lists):
            min_value = float("inf")
            for i in range(len(temp_list)):
                curr = temp_list[i]
                if curr:
                    if curr.val < min_value:
                        min_index = i
                        min_value = curr.val

            # print("count_none = ", count_none)
            # print(min_index, temp_list[min_index].val)
            # self.print_linked_list(head)

            min_node = temp_list[min_index]
            temp_list[min_index] = temp_list[min_index].next
            if not temp_list[min_index]:
                count_none = count_none + 1

            min_node.next = None

            if not head:
                head = min_node
                prev = min_node
            else:
                prev.next = min_node
                prev = prev.next
        return head


# Issues with my solution:
#   unnecessary confusion to set head node
#   difficult setup of checking if nodes parsing is complete in any ll
#   O(N) check to get current smallest node

# Best solution:
# ** Uses a heap to find the lowest current node in each linked list
# ** Sets a dummy node as head and then returns dummy.next in the end

# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class HeapNode:
#     def __init__(self, node):
#         self.node = node

#     def __lt__(self, other):
#         # Define comparison based on ListNode's value
#         return self.node.val < other.node.val


# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         dummy = ListNode(0)
#         current = dummy
#         heap = []

#         # Initialize the heap
#         for l in lists:
#             if l:
#                 heapq.heappush(heap, HeapNode(l))

#         # Extract the minimum node and add its next node to the heap
#         while heap:
#             heap_node = heapq.heappop(heap)
#             node = heap_node.node
#             current.next = node
#             current = current.next
#             if node.next:
#                 heapq.heappush(heap, HeapNode(node.next))

#         return dummy.next
