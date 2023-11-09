class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # Create a dummy node and connect it to the head of the original list
        dummy = ListNode(next=head)
        # Initialize two pointers: prev and curr
        prev, curr = dummy, head
        
        # Iterate through the list
        while curr:
            # Store the next node in the list
            nxt = curr.next
            
            # Check if the current node's value matches the target value (val)
            if curr.val == val:
                # If yes, skip the current node by updating prev's next pointer
                prev.next = nxt
            else:
                # If no, update prev to point to the current node
                prev = curr
            
            # Move to the next node in the list
            curr = nxt
        
        # Return the next of the dummy node, which is the modified list
        return dummy.next
