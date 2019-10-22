class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def add(self, l: ListNode) -> int:
        res = ''
        current = l
        while current != None:
            res = str(current.val) + res
            current = current.next
        return int(res)
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val = str(self.add(l1) + self.add(l2))
        l3 = ListNode(val[0])
        
        if len(val) > 1:
            for number in val[1:]:
                temp = ListNode(int(number))
                temp.next = l3
                l3 = temp

        return l3
        


s = Solution()
l1, l2 = ListNode(2), ListNode(5)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

l = s.addTwoNumbers(l1, l2)

# print(l)
print(l.val)
print(l.next.val)
print(l.next.next.val)