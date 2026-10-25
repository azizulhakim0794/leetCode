# python 203_Remove_Linked_List_Elements.py


# head = [1, 2, 6, 3, 4, 5, 6]
val = 6
# Output: [1,2,3,4,5]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


values = [1, 2, 6, 3, 4, 5, 6]

head = ListNode(values[0])

current = head

for value in values[1:]:
    current.next = ListNode(value)
    current = current.next


def removed_items(head, val):
    curr = head
    prev = None

    while curr:
        if curr.val == val:
            if prev:
                prev.next = curr.next
            else:
                head = curr.next
        else:
            prev = curr
        curr = curr.next

    return head


removed_items(head, val)

current = head

while current:
    print(current.val)
    current = current.next
