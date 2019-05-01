from random import randint, randrange
from SinglyLinkedNode import Node, insert_node, stringify_linked_list, list_length

def test_remove_dups():

    from remove_dups import remove_dups, remove_dups_alternative

    def print_lists():
        print("0) Length of list {} is {}".format(stringify_linked_list(head0), list_length(head0)))
        print("1) Length of list {} is {}".format(stringify_linked_list(head1), list_length(head1)))
        print("2) Length of list {} is {}".format(stringify_linked_list(head2), list_length(head2)))

    head0 = None
    head1 = None
    head2 = None
    for _ in range(5):
        head0 = insert_node(head0, 2)
        head1 = insert_node(head1, randrange(10))
        head2 = insert_node(head2, randrange(10))

    print_lists()
    print("...removing dups...")
    remove_dups(head0)
    remove_dups(head1)
    remove_dups_alternative(head2)
    print_lists()

def test_kth_to_last():
    
    pass

def test_sum_lists():
    
    from sum_lists import sum_lists, sum_lists_alt

    head1 = None
    head2 = None
    for _ in range(5):
        head1 = insert_node(head1, randrange(1, 10))
        head2 = insert_node(head2, randrange(1, 10))
    sum1 = sum_lists(head1, head2)
    sum2 = sum_lists_alt(head1, head2, 0)
    print(stringify_linked_list(head1))
    print(stringify_linked_list(head2))
    print("sum_iterative: {}".format(stringify_linked_list(sum1)))
    print("sum_recursive: {}".format(stringify_linked_list(sum2)))

if __name__ == "__main__":
    test_sum_lists()