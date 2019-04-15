class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

def insert_node(head, new_value):
    node = Node(new_value)
    end = head or None
    if end is not None:
        while end.next_node is not None:
            end = end.next_node
        end.next_node = node
    else:
        return node
    return head

def stringify_linked_list(head):
    display_str = ''
    while head is not None:
        display_str += str(head.value) + "->"
        head = head.next_node
    display_str += "None"
    return display_str

def list_length(node):
    length = 0
    while node is not None:
        length += 1
        node = node.next_node
    return length