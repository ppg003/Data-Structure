class TreeNode:
    def __init__(self, l=None, val=None, r=None):
        self.l = l
        self.val = val
        self.r = r


class huofuman:
    def __init__(self, list_node=None):
        self.root = self.build_tree(list_node)

    def build_tree(self, list_node):
        # leaf
        node_par = None
        node_leaf_l = list_node[0]
        del list_node[0]
        node_leaf_r = list_node[0]
        del list_node[0]
        while 1:
            sum = node_leaf_l.val + node_leaf_r.val
            node_par = TreeNode(node_leaf_l, sum, node_leaf_r)
            if len(list_node) == 0:
                break
            node_new = list_node[0]
            del list_node[0]
            if node_new.val > node_par.val:
                node_leaf_l = node_par
                node_leaf_r = node_new
            else:
                node_leaf_l = node_new
                node_leaf_r = node_par
        return node_par

    def WPL(self, node=None, layer=0):
        if node is None:
            node = self.root
        if node.l is None and node.r is None:
            return node.val * layer
        wpl_l, wpl_r = 0, 0
        if node.l is not None:
            wpl_l = self.WPL(node.l, layer + 1)
        if node.r is not None:
            wpl_r = self.WPL(node.r, layer + 1)
        return wpl_l + wpl_r

n1 = TreeNode(val=2)
n2 = TreeNode(val=4)
n3 = TreeNode(val=5)
n4 = TreeNode(val=15)
list_node = [n1, n2, n3, n4]
x = huofuman(list_node)
# print(x.root.val)
print(x.WPL())
