# python 876_Middle_of_the_Linked_List.py

# head = [1, 2, 3, 4, 5]
# Output: [3,4,5]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


values = [1, 2, 3, 4, 5, 6]

head = ListNode(values[0])

current = head

for value in values[1:]:
    current.next = ListNode(value)
    current = current.next


# def find_middle_length(head):
#     count = 0
#     current = head

#     while current:
#         count += 1
#         current = current.next

#     if count % 2 == 0:
#         return int((count / 2) + 1)
#     else:
#         return int((count / 2) + 1)


# mid = find_middle_length(head)


def find_middle_last_list(head):

    def find_middle_length(head):
        count = 0
        current = head

        while current:
            count += 1
            current = current.next

        return (count // 2) + 1

    mid = find_middle_length(head)
    current = head
    count = 1

    while current:
        if count == mid:
            return current

        current = current.next
        count += 1

    return head


current = find_middle_last_list(head)

while current:
    print(current.val)
    current = current.next
