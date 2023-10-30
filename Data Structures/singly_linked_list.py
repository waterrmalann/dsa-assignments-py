class Node:
    def __init__(self, val):
        self.value = val  # store the value of the node
        self.next = None  # store the address to the next node

class SinglyLinkedList:
    def __init__(self):
        # Initialize with an empty head and tail.
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        # Add an element to the end of the list.
        new_node = Node(value)
        if not self.head:
            # If the list is empty.
            # Both the head and the tail are the new node.
            self.head = new_node
            self.tail = self.head
        else:
            # Otherwise, we redirect the tail towards new node.
            self.tail.next = new_node
            # Update the tail of the list as well.
            self.tail = new_node
            # Increase the length of the list and return the list.
            self.length += 1
        return self

    def pop(self):
        # Remove an element from the end of the list.
        # If we have an empty list, we return None.
        if not self.head:
            return None
        # We have to loop until the second-last element.
        current = self.head  # starting from the head
        second_last = current
        while current.next:
            # As long as the current node has a next node.
            second_last = current  # store the second-last node
            current = current.next  # move the current pointer up
        # Make the second last node point to None.
        second_last.next = None
        # Update the tail of the list.
        self.tail = second_last
        self.length -= 1
        if self.length == 0:
            # If we end up with an empty list, invalidate the head and tail.
            self.head = None
            self.tail = None
        # Return the popped element.
        return current

    def unshift(self, value):
        # Add an element to the start of the list.
        new_node = Node(value)
        if not self.head:
            # If our list is empty, head and tail are equal to the new node.
            self.head = new_node
            self.tail = self.head
        else:
            # Make the new node point towards the current head.
            new_node.next = self.head
            # Update the current head.
            self.head = new_node
            # Increase the list length and return the list.
            self.length += 1
        return self

    def shift(self):
        # Remove an element from the start of the list.
        removed = self.head
        self.head = removed.next
        self.length -= 1
        if self.length == 0:
            # If our list is empty, we invalidate the tail.
            # The head would automatically be None.
            self.tail = None
        return removed

    def get(self, index):
        # Get an element by index.
        if index < 0 or index >= self.length:
            return None
        counter = 0  # Need to start at the first index.
        current = self.head  # and from the head.
        while counter != index:
            # Run a loop until the counter equals the target index.
            current = current.next  # Advance the node.
            counter += 1  # Increment the counter
        return current

    def set(self, index, value):
        # Set an element by index.
        # Get the element by index since we have a self.get()
        node = self.get(index)
        if node:
            # Assuming our target node is not None.
            node.value = value
            return True
        # Otherwise, we return False because nothing was set.
        return False

    def insert(self, index, value):
        # Insert an element into the index position.
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return bool(self.unshift(value))
        if index == self.length:
            return bool(self.push(value))

        # Get the element right before our target node.
        node_before = self.get(index - 1)
        point_to = node_before.next  # The node to point our new node at.
        # Create a new node.
        new_node = Node(value)
        node_before.next = new_node  # Node before the target node should point to the new node.
        new_node.next = point_to  # New node needs to point at the displaced node.
        self.length += 1  # Increment the length
        return True

    def remove(self, index):
        # Remove an element from the index position.
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return bool(self.shift())
        if index == self.length - 1:
            return bool(self.pop())

        # Grab the element before our target.
        node_before = self.get(index - 1)
        removed_node = node_before.next  # Node to remove.
        node_before.next = removed_node.next  # Redirect the arrows to skip the index.
        self.length -= 1  # Decrement the length as we removed an element.
        return True

    def reverse(self):
        # Reverse the list in place.
        # We need three pointers: current, previous, and next.
        prev = None
        current = self.head
        while current:
            # Run the loop until the end of the list.
            next_node = current.next  # Store the next node.
            current.next = prev  # Point the current node back.
            prev = current  # Advance the previous node.
            current = next_node  # Advance the current node.
        # Let's swap the head and tail.
        self.head, self.tail = self.tail, self.head
        return True

    def to_array(self):
        # Print the list (represented as a list)
        arr = []
        current = self.head
        while current:
            arr.append(current.value)
            current = current.next
        return arr