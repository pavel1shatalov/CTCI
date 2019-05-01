def delete_middle(node):
    if node == None or node.next_node == None:
        return False
    node.value = node.next_node.value
    node.next_node = node.next_node.next_node