"""
Given the head of a singly linked list, group all the nodes with odd indices 
Together followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain 
As it was in the input. You must solve the problem in O(1) extra space 
complexity and O(n) time complexity.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
"""
# Solution 1

def oddEvenList(head):
    if not head:
        return 
    
    prev = None
    cur = head
    temp = head.next
    count = 1

    while cur and cur.next:
        prev = cur 
        cur = cur.next
        prev.next = cur.next
        count += 1
    
    if count % 2 == 0:
        prev.next = temp
    else:
        cur.next = temp

    return head

# Solution 2

def oddEvenList_1(head):
    if not head:
        return
    
    first = head
    second_head = second = head.next
    while first.next and second.next:
        first.next, second.next = first.next.next, second.next.next
        first = first.next
        second = second.next
    first.next = second_head
    return head 