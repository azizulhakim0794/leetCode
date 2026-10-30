# python 21_Merge_Two_Sorted_Lists.py
# list1 = [1, 2, 4]
# list2 = [1, 3, 4]
# Output: [1,1,2,3,4,4]


list1 = []
list2 = [0]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head1 = ListNode(list1[0])

current1 = head1

for value in list1[1:]:
    current1.next = ListNode(value)
    current1 = current1.next

head2 = ListNode(list2[0])

current2 = head2

for value in list2[1:]:
    current2.next = ListNode(value)
    current2 = current2.next


def marge_list(head1, head2):
    temp = ListNode(0)
    current = temp

    list1 = head1
    list2 = head2
    # these conditions works in the leetcode only here have some value assign relaed problems
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

        if list1:
            current.next = list1
        if list2:
            current.next = list2

    return temp.next


current = marge_list(head1, head2)

while current:
    print(current.val)
    current = current.next
