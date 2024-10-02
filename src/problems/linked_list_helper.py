class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
        while temp:
            end = "," if temp.next else "\n"
            print(temp.val, end=end)
            temp = temp.next

    def create_list(self, arr):
        head = None
        tail = None
        for n in arr:
            Node = ListNode(n)
            if not head:
                head = Node
            if not tail:
                tail = Node
                continue
            tail.next = Node
            tail = Node
        return head
