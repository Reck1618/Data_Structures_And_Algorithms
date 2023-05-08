"""
Given the head of a Singly LinkedList that contains a cycle, 
write a function to find the starting node of the cycle.
"""

from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()


def find_cycle_start(head):
    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            count = cycle_count(slow)
            break
    return start(head, count)

def cycle_count(slow):
    cur_pointer = slow
    count = 0

    while True:
        cur_pointer = cur_pointer.next
        count += 1

        if cur_pointer == slow:
            break
    return count

def start(head,count):
    pointer_1 = head
    pointer_2 = head

    while count > 0:
        pointer_2 = pointer_2.next
        count -= 1
    
    while pointer_1 != pointer_2:
        pointer_1 = pointer_1.next
        pointer_2 = pointer_2.next
    return pointer_2

# Time Complexity : O(N)
# Space Complexity : O(1)


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()