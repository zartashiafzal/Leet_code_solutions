class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize the current pointer to the head of the linked list
        cur = head
        
        # Outer loop: Traverse through the linked list until cur is not null
        while cur:
            # Inner loop: Check if cur has duplicates (cur.next with same value)
            while cur.next and cur.next.val == cur.val:
                # Remove duplicates by bypassing the next node/ updating cur.next
                cur.next = cur.next.next
            # Move to the next node to check for duplicates
            cur = cur.next
        
        # Return the modified head of the linked list after removing duplicates
        return head

