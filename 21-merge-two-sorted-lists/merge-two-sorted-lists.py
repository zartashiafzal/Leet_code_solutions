class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node and a tail reference to track the current position
        dummy = ListNode()
        tail = dummy
        
        # Iterate while both lists have elements
        while l1 and l2:
            # Compare values from both lists
            if l1.val < l2.val:
                # If value from l1 is smaller, link it to the result and move l1 pointer
                tail.next = l1
                l1 = l1.next
            else:
                # If value from l2 is smaller or equal, link it to the result and move l2 pointer
                tail.next = l2
                l2 = l2.next
            # Move the result pointer to the newly added node
            tail = tail.next
        
        # Link the remaining elements from either list (if any)
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        
        # Return the merged list starting from the next of the dummy node
        return dummy.next
