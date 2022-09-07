class Node():
    ## Only support int so far
    def __init__(self, data):
        if data is None:
            raise ValueError("data is None")

        if type(data) is not int:
            raise ValueError(f"data must be int: {data}")

        self.data   = data
        self.left   = None
        self.right  = None


    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


    def print(self):
        print(self.data)


    def print_depth_first(self):
        # depth first print
        if self.left is not None:
            self.left.print_depth_first()
        if self.right is not None:
            self.right.print_depth_first()
        self.print()


class BT():
    ## For this BT, only distinct values exists.
    def __init__(self, data):
        new_node = Node(data)
        self.head_node = new_node


    def display(self):
        lines, *_ = self.head_node._display_aux()
        for line in lines:
            print(line)


    def print_tree_depth_first(self):
        self.head_node.print_depth_first()


    def print_tree_breadth_first(self):
        queue = [self.head_node]
        while len(queue) != 0:
            first_out = queue.pop(0)
            if first_out.left is not None:
                queue.append(first_out.left)
            if first_out.right is not None:
                queue.append(first_out.right)
            first_out.print()


    def insert_helper(self, node, data):
        # Can assume node is not None
        if data == node.data:
            print(f'{data} already is in BT')
            return

        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_helper(node.left, data)

        else:
            # data > node.data
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_helper(node.right, data)


    def insert(self, data):
        node = self.head_node

        if node is None:
            self.head_node = Node(data)

        if data == node.data:
            print(f'{data} already is in BT')
            return

        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_helper(node.left, data)

        else:
            # data > node.data
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_helper(node.right, data)


    def remove(self, data):
        ...


    def balance_tree(self):
        ...

bt = BT(5)
bt.print_tree_depth_first()
print('....')
bt.print_tree_breadth_first()
print('--------------')

bt.insert(2)
bt.insert(23)
bt.print_tree_depth_first()
print('....')
bt.print_tree_breadth_first()
print('--------------')

bt.insert(3)
bt.print_tree_depth_first()
print('....')
bt.print_tree_breadth_first()
print('--------------')

bt.insert(3)
bt.print_tree_depth_first()
print('....')
bt.print_tree_breadth_first()
print('--------------')

bt.display()