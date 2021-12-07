from node import Node

if __name__ == "__main__":

    # Create a linked list
    # use __iter__ to iterate over the linked list
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for child in root:
        print(child)

    # create a list of nodes using list comprehension
    list_of_nodes = [node for node in root]
    print(list_of_nodes)

    # create a list of nodes using generator expression
    print("-" * 20)
    print("Generator")
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    for ch in root.depth_first():
        # Outputs Node(0), Node(1), Node(3), Node(4), Node(2), Node(5)
        print(ch)
    list_of_nodes = [node for node in root.depth_first()]
    print(list_of_nodes)

    list_of_nodes = list(root.depth_first())

    # create a dictionary of nodes using dundur method
    root_dict = root.__dict__

    print(root_dict)
    
    print("-" * 20)
    print("")
