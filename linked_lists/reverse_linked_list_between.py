def reverseBetween(head, m, n):
    if not head:
        return None
    # Reverse the linked list only in between
    current_node = head
    previous_node = None
    next_node = None

    while m > 1:
        previous_node = current_node
        current_node = current_node.next
        m, n = m - 1, n - 1

    tail_node, connecting_node = current_node, previous_node

    while n:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
        n -= 1

    if connecting_node:
        connecting_node.next = previous_node
    else:
        head = previous_node

    tail_node.next = current_node
    return head
