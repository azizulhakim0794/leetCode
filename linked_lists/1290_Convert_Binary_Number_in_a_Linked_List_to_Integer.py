# python 1290_Convert_Binary_Number_in_a_Linked_List_to_Integer.py


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


values = [1, 0, 1]
# Output: 5 convert to base 10

head = ListNode(values[0])

current = head

for value in values[1:]:
    current.next = ListNode(value)
    current = current.next


def cocvert_to_binary(head):
    current = head
    nums = ""
    result = 0

    while current:
        nums += str(current.val)
        current = current.next

    print(int(nums))
    for num in nums:
        result = result * 2 + int(num)

    return result


cocvert_to_binary(head)
