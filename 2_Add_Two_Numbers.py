# python 2_Add_Two_Numbers.py


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


li1 = [2, 4, 3]
li2 = [5, 6, 4]

head1 = ListNode(li1[0])

current1 = head1

for value in li1[1:]:
    current1.next = ListNode(value)
    current1 = current1.next

head2 = ListNode(li2[0])

current2 = head2

for value in li2[1:]:
    current2.next = ListNode(value)
    current2 = current2.next


def reverse_linked_list(head):
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


head = reverse_linked_list(head1)
print(head)

current = head

while current:
    print(current.val)
    current = current.next
