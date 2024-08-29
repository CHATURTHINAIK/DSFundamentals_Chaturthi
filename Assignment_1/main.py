from list_code import *
def main():

    # create a new linked list
    llist = LinkedList()

    # add nodes to the linked list
    llist.insertAtEnd(1)
    llist.insertAtEnd(2)
    llist.insertAtEnd(3)
    llist.insertAtEnd(4)
    # llist.insertAtEnd(5)
    llist.insertAtEnd(6)
    llist.insertAtEnd(7)
    llist.insertAtEnd(8)
    llist.insertAtEnd(9)
    llist.insertAtEnd(10)

    print("Node Data")
    llist.printLL()

    print("\nMiddle Element of linked list :", end=" ")
    size = llist.sizeOfLL()

    # find middle element
    if size%2 == 0:
        index = size/2
    else:
        index = (size+1)/2

    # print(llist.sizeOfLL())


    llist.find_middle_element(index)

main()