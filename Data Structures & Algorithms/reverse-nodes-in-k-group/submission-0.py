# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def findKthNode(self, curr, k):
        while curr and k>1:
            curr = curr.next
            k-=1
        return curr
    
    def reverse(self, curr):
        prev = None
        while curr:
            tmp = curr
            curr = curr.next
            tmp.next = prev
            prev = tmp
        return prev



    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prevNode = nextNode = None

        while True:
            kthNode = self.findKthNode(temp,k)
            if not kthNode:
                if prevNode:
                    prevNode.next = temp
                break
            nextNode = kthNode.next
            kthNode.next = None
            self.reverse(temp)
            if temp == head:
                head = kthNode
            else:
                prevNode.next = kthNode
            prevNode = temp
            temp = nextNode
        return head

        