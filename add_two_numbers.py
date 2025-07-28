# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

next_l1 = ListNode(val=9)
next_l2 = ListNode(val=9)

def generateLinkedList(length, values):
    i = length
    next_l = ListNode(val=values[i-1])
    while i > 1:
        i -= 1
        l = ListNode(val=values[i-1], next=next_l)
        next_l = l
    return l

l1 = generateLinkedList(5, [9]*5)
l2 = generateLinkedList(7, [9]*7)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        _sum = 0
        cycles = 0
        node1, node2 = l1, l2 

        while node1 is not None and node2 is not None:
            _sum += node1.val * (10 ** cycles)  + node2.val * (10 ** cycles)
            node1, node2 = node1.next, node2.next
            cycles += 1

        if node1 is None:
            while node2 is not None:
                _sum += node2.val * (10 ** cycles)
                node2 = node2.next
                cycles += 1
        else:
            while node1 is not None:
                _sum += node1.val * (10 ** cycles)
                node1 = node1.next
                cycles += 1

        if _sum == 0: return ListNode()
        if _sum // 10 == 0: return ListNode(val=_sum)

        digits = []
        i = 0
        while _sum > 0:
            digits.append(_sum % 10)
            _sum //= 10
            i += 1
        
        i = len(digits)-1

        next_l = ListNode(val=digits[i])
        while i > 0:
            i -= 1
            l = ListNode(val=digits[i], next=next_l)
            next_l = l

        return l

def addTwoNumbers(l1, l2):
    _sum = l1.val + l2.val
    n1, n2 = l1.next, l2.next
    tens = _sum // 10
    n3 = ListNode(val=_sum % 10)
    head_n3 = n3

    while n1 is not None and n2 is not None:
        _sum = n1.val + n2.val + tens
        n1, n2 = n1.next, n2.next
        tens = _sum // 10
        next_n3 = ListNode(val = _sum % 10)
        n3.next = next_n3
        n3 = next_n3
    
    if n1 is None:
        while n2 is not None:
            n3.next = n2
            n2 = n2.next
    else:
        while n1 is not None:
            n3.next = n1
            n1 = n1.next
    
    return head_n3
