# python linked_list.py


# first way
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# # Create nodes
# first = ListNode(10)
# second = ListNode(20)
# third = ListNode(30)
# fourth = ListNode(40)
# fifth = ListNode(50)
# sixth = ListNode(60)

# # Connect nodes
# # first.next = second
# # second.next = third

# # Store all nodes in a list
# nodes = [first, second, third, fourth, fifth, sixth]

# # Connect nodes dynamically
# for i in range(len(nodes) - 1):
#     nodes[i].next = nodes[i + 1]


# # Print the linked list
# current = first

# while current:
#     print(current.val)
#     current = current.next

#
#
# end first method
#
#


# start searching and also find the length


# values = [10, 20, 30, 40, 50, 60]
# s = 41
# list_length = 1
# # Outpur: True

# head = ListNode(values[0])
# current = head

# # print(values[1:])

# for value in values[1:]:
#     current.next = ListNode(value)
#     current = current.next
#     list_length += 1

# current = head

# count = 1

# while current:
#     if current.val == s:
#         print(True)
#         break
#     elif list_length == count:
#         print(False)
#     count += 1
#     current = current.next
#
#
# Insert at the beginning
#
#

# values = [30, 40, 50, 60, 70]

# head = ListNode(values[0])

# current = head

# for value in values[1:]:
#     current.next = ListNode(value)
#     current = current.next

# current = head

# while current:
#     print(current.val)
#     current = current.next


# def linked_list_length(head):
#     count = 0
#     current = head

#     while current:
#         count += 1
#         current = current.next

#     print(count)


# linked_list_length(head)


#
#
# reverse linked list
#
#

values = [30, 40, 50, 60, 70]

head = ListNode(values[0])

current = head

for value in values[1:]:
    current.next = ListNode(value)
    current = current.next


def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    return prev


# [30, 40, 50, 60, 70]


# current = head

head = reverse_linked_list(head)

current = head


while current:
    print(current.val)
    current = current.next
