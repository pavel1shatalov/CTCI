import SinglyLinkedNode as sln

def sum_lists(node1, node2):
    carry = 0
    head = None
    runner = None
    while node1 is not None or node2 is not None:
        if head is None:
            head = sln.Node(0, None)
            runner = head
        else:
            runner.next_node = sln.Node(0, None)
            runner = runner.next_node
        sum = 0
        if node1 is not None:
            assert(node1.value < 10)
            sum += node1.value
            node1 = node1.next_node
        if node2 is not None:
            assert(node2.value < 10)
            sum += node2.value
            node2 = node2.next_node
        sum += carry
        carry = 0
        if sum > 9:
            carry = sum // 10
            sum = sum - 10
        runner.value = sum
    if carry > 0:
        runner.next_node = sln.Node(carry, None)
    return head

def sum_lists_alt(node1, node2, carry):
    if (node1 is None and node2 is None and carry == 0):
        return None
    sum = carry
    head = sln.Node(0, None)
    if node1 is not None:
        assert(node1.value < 10)
        sum += node1.value
    if node2 is not None:
        assert(node2.value < 10)
        sum += node2.value
    head.value = sum % 10
    after_head = sum_lists_alt( None if node1 is None else node1.next_node, \
                                None if node2 is None else node2.next_node, \
                                1 if sum >= 10 else 0)
    head.next_node = after_head
    return head
