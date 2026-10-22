class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


values = [30, 40, 50, 60, 70]

head = ListNode(values[0])

current = head

for value in values[1:]:
    current.next = ListNode(value)
    current = current.next


def reverse_linked_list(head):
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


reverse_linked_list(head)
