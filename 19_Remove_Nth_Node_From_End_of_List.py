# python 19_Remove_Nth_Node_From_End_of_List.py
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


values = [1, 2, 3, 4, 5]
n = 2

head = ListNode(values[0])

current = head

for value in values[1:]:
    current.next = ListNode(value)
    current = current.next


def removed_items(head, n):
    curr = head
    prev = None
    n_th_item = 0

    def find_length(head):
        curr = head
        length = 1

        while curr:
            length += 1
            curr = curr.next
        return length

    item_len = find_length(head)

    n_th_item = item_len - n - 1

    for i in range(item_len - 1):
        if i == n_th_item:
            if prev:
                prev.next = curr.next
            else:
                head = curr.next
        else:
            prev = curr
        curr = curr.next

    return head


current = removed_items(head, n)

while current:
    print(current.val)
    current = current.next
