from LinkedList import LinkedList

# Time: O(n)
# Space: O(n)

def remove_dups(head):
    hash_table = {head.data: True}
    while head:
        if head.next is None:
            break
        if hash_table.get(head.next.data):
            head.next = head.next.next
        else:
            hash_table[head.next.data] = True
            head = head.next

# Time: O(n^2)
# Space: O(1)
  
def remove_dups_alternative(head):
    while head:
        runner = head
        while runner:
            if runner.next is None:
                break
            if runner.next.data == head.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        head = head.next

# Test

if __name__ == '__main__':

    lst1 = LinkedList()
    lst2 = LinkedList()
    for _ in range(5):
        lst1.append(3)
        lst2.append(4)
    print(lst1)
    print(lst2)
    remove_dups(lst1.head)
    remove_dups_alternative(lst2.head)
    print(lst1)
    print(lst2)
