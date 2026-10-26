# python 2_Add_Two_Numbers.py


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


li1 = [5, 6]
li2 = [5, 4, 9]

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
    curr = head
    num = ""

    while curr:
        num += str(curr.val)
        curr = curr.next

    return int(num[::-1])


num1 = reverse_linked_list(head1)
num2 = reverse_linked_list(head2)

total = num1 + num2

result = str(total)[::-1]

sum_head = ListNode(int(result[0]))
curr3 = sum_head

for value in result[1:]:
    curr3.next = ListNode(int(value))
    curr3 = curr3.next

curr3 = sum_head

while curr3:
    print(curr3.val)
    curr3 = curr3.next
