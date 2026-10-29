# python 237_Delete_Node_in_a_Linked_List.py
# head = [4, 5, 1, 9]

# [4,1,9]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


values = [4, 5, 1, 9]
node = 1


head = ListNode(values[0])

current = head

for value in values[1:]:
    current.next = ListNode(value)
    current = current.next


def delete_node(head, node_val):

    # this is the actual code
    # if node is None or node.next is None:
    #         return

    # node.val = node.next.val
    # node.next = node.next.next
    current = head

    while current and current.next:
        if current.next.val == node_val:
            current.next = current.next.next
        else:
            current = current.next
    return head


current = delete_node(head, node)

while current:
    print(current.val)
    current = current.next
