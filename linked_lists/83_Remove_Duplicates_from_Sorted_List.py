# python 83_Remove_Duplicates_from_Sorted_List.py
# first way
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


values = [30, 40, 40, 50, 60, 70]

head = ListNode(values[0])

current = head

for value in values[1:]:
    current.next = ListNode(value)
    current = current.next


def duplicateItem(head):
    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head


current = duplicateItem(head)

while current:
    print(current.val)
    current = current.next
