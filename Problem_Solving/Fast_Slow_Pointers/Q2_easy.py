"""
Given the head of a LinkedList with a cycle, find the length of the cycle.
"""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def find_cycle_length(head):
    fast, slow = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            return calculate_length(slow)
    return 0

def calculate_length(slow):
    count = 0
    cur_pointer = slow
    while True:
        cur_pointer = cur_pointer.next
        count += 1

        if cur_pointer == slow:
            break
    return count
 


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle length: " + str(find_cycle_length(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle length: " + str(find_cycle_length(head)))


main()
