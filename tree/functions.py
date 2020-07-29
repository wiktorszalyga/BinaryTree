from .models import Node


def add_node(name, value):
    # Adding new node
    root_set = Node.objects.all()
    if root_set:
        index = len(root_set)

        for x in range(index):
            if root_set[x].left:
                if root_set[x].right:
                    continue
                else:
                    new_node = Node.objects.create(id=index, name=name, value=value, right=None, left=None)
                    Node.objects.filter(id=x).update(right=new_node)
                    return
            else:
                new_node = Node.objects.create(id=index, name=name, value=value, right=None, left=None)
                Node.objects.filter(id=x).update(left=new_node)
                return

    else:
        new = Node.objects.create(id=0, name=name, value=value, left=None, right=None)


def edit_node(name, value, index):
    # Edit node
    if name and value:
        node = Node.objects.filter(id=index).update(name=name, value=value)
    elif name and not value:
        node = Node.objects.filter(id=index).update(name=name)
    elif not name and value:
        node = Node.objects.filter(id=index).update(value=value)


def delete_node(index):
    root_set = Node.objects.all()
    size = len(root_set) - 1

    if index == size:
        del_node = Node.objects.filter(id=index).delete()
    else:
        swap(index, size)
        del_node = Node.objects.filter(id=size).delete()


def sort_all_nodes(root_set):
    # Sort all nodes in trees with modify bubble sort
    if root_set:
        size = len(root_set) - 1
        for index in range(size, -1, -1):
            bubble(index, root_set, size)


# def sort_select_nodes(root_set, index):
#

def bubble(index, root_set, size):
    # Modify bubble sort
    root_set = Node.objects.all()
    if index >= 1:
        if index % 2 == 0:
            print('Bubble po modulo == 0 node: {}'.format(root_set[index]))
            if root_set[index].value > root_set[int(index/2) - 1].value:
                print('Bubble po indeks wiekszy od rodzica node: {}'.format(root_set[index]))
                swap(index, int(index/2) - 1)
                print('Bubble po swapie node: {}'.format(root_set[index]))
                down_check(index, size)
                bubble(int(index/2) - 1, root_set, size)
        else:
            print('Bubble po modulo == 1 node: {}'.format(root_set[index]))
            if root_set[index].value > root_set[int(index/2)].value:
                print('Bubble po indeks wiekszy od rodzica node: {}'.format(root_set[index]))
                swap(index, int(index/2))
                print('Bubble po swapie node: {}'.format(root_set[index]))
                down_check(index, size)
                bubble(int(index/2), root_set, size)


def down_check(index, size):
    # Allow to sort nodes which were swap in time of sorting another node
    root_set = Node.objects.all()
    check_index_left = 2*(index + 1) - 1
    check_index_right = 2 * (index + 1)
    print('Down check')
    if check_index_left <= size and root_set[index].value < root_set[check_index_left].value and \
            root_set[check_index_left].value > root_set[check_index_right].value:

        print('Chech | lewy większy wszedł index: {}'.format(root_set[index]))
        print('Chech | lewy większy wszedł left: {}'.format(root_set[check_index_left]))
        swap(index, check_index_left)
        down_check(check_index_left, size)
    elif check_index_right <= size and root_set[index].value < root_set[check_index_right].value:
        print('Chech | lewy większy wszedł index: {}'.format(root_set[index]))
        print('Chech | lewy większy wszedł left: {}'.format(root_set[check_index_left]))
        swap(index, check_index_right)
        down_check(check_index_right, size)


def swap(id_1, id_2):
    # Exchange between two nodes
    node_1 = Node.objects.filter(id=id_1)
    node_2 = Node.objects.filter(id=id_2)
    tmp_value = node_1[0].value
    tmp_name = node_1[0].name
    tmp_value_2 = node_2[0].value
    tmp_name_2 = node_2[0].name
    node_1.update(name=None, value=None)
    node_2.update(name=tmp_name, value=tmp_value)
    node_1.update(name=tmp_name_2, value=tmp_value_2)


def count_level(root):
    # Returning height of tree
    level = 0
    done = True

    while done:
        if root.left:
            level += 1
            root = root.left
        else:
            done = False
    return level


def get_parent(root_set):
    # Return two related lists of names of nodes and parents of these nodes

    if root_set:
        nam = root_set[0].name + ' : ' + str(root_set[0].value)
        name = [nam]
        parent = [""]

        for node in root_set:

            if node.left_set.all():
                pam = node.left_set.get().name + ' : ' + str(node.left_set.get().value)
                parent.append(pam)
                nam = node.name + ' : ' + str(node.value)
                name.append(nam)

            if node.right_set.all():
                pam = node.right_set.get().name + ' : ' + str(node.right_set.get().value)
                parent.append(pam)
                nam = node.name + ' : ' + str(node.value)
                name.append(nam)
    else:
        name = []
        parent = []

    return name, parent
