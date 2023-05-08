"""
Given the head of a Singly LinkedList, write a method to modify the LinkedList such 
that the nodes from the second half of the LinkedList are inserted alternately to 
the nodes from the first half in reverse order. So if the LinkedList has nodes 
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should 
return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

Your algorithm should not use any extra space and the input LinkedList 
should be modified in-place.

Example-1
Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null 
"""
from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(str(temp.value) + " ", end='')
      temp = temp.next
    print()


def reorder(head):
  fast, slow = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  
  head_second = reverse(slow)
  head_first = head

  while head_second is not None and head_first is not None:
    temp = head_first.next
    head_first.next = head_second
    head_first = temp

    temp = head_second.next
    head_second.next = head_first
    head_second = temp
  
  if head_first is not None:
    head_first.next = None

def reverse(head):
  prev = None
  while head:
    temp = head
    head = head.next
    temp.next = prev
    prev = temp
  return prev


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.next.next.next.next.next = Node(12)
  reorder(head)
  head.print_list()


main()