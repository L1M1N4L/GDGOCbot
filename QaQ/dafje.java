/**
 * Node class to represent a node in the linked list
 */
class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        next = null;
    }
}

/**
 * LinkedList class with the deleteNode function
 */
class LinkedList {
    Node head;

    /**
     * Function to delete a node with the given value from the linked list
     * @param value the value to be deleted
     * @return the updated head of the linked list
     */
    Node deleteNode(int value) {
        // Initialize pointers
        Node temp = head;
        Node prev = null;

        // Check if the head node itself holds the value to be deleted
        if (temp != null && temp.data == value) {
            head = temp.next; // Changed head
            return head;
        }

        // Search for the value to be deleted
        while (temp != null && temp.data != value) {
            prev = temp;
            temp = temp.next;
        }

        // If the value was not present in the linked list
        if (temp == null) {
            return head;
        }

        // Unlink the node from the linked list
        prev.next = temp.next;

        return head;
    }

    // Example usage:
    public static void main(String[] args) {
        LinkedList list = new LinkedList();

        // Create the linked list: 10 -> 20 -> 30 -> 40 -> null
        list.head = new Node(10);
        Node second = new Node(20);
        Node third = new Node(30);
        Node fourth = new Node(40);

        list.head.next = second;
        second.next = third;
        third.next = fourth;

        // Delete the node with value 30
        list.head = list.deleteNode(30);

        // Print the updated list: 10 -> 20 -> 40 -> null
        Node current = list.head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
    }
}