# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# from json import dumps, loads

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        non_null_nodes = 1
        q = [root]
        left = 0
        right = 1
        stream = []
        while left < right and non_null_nodes > 0:
            curr = q[left]
            left+=1
            right+=2
            stream.append(curr.val if curr else None)
            if curr is None:
                continue
            non_null_nodes -= 1
            q.append(curr.left)
            q.append(curr.right)
            if curr.left and curr.right:
                non_null_nodes +=2
                continue
            if not curr.left and not curr.right:
                continue
            non_null_nodes += 1
        return dumps(stream)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # if len(data) == 2:
        #     return None
        # data_list = data[1:len(data)-1].split(",")
        # data_list = [int(x) if x.strip().isdecimal() else "None" for x in data_list]
        data_list = loads(data)
        # print(data_list)
        i = 0
        j = 1
        if not data_list:
            return None
        root = TreeNode(data_list[0])
        node_list = [root]
        while j < len(data_list):
            if node_list[i] == None:
                i+=1
                continue
            if data_list[j] is None:
                node_list[i].left = None
                node_list.append(None)
            else:
                new_element = TreeNode(data_list[j])
                node_list[i].left = new_element
                node_list.append(new_element)
            j = j + 1
            if j == len(data_list):
                break
            if data_list[j] is None:
                node_list[i].right = None
                node_list.append(None)
            else:
                new_element = TreeNode(data_list[j])
                node_list[i].right = new_element
                node_list.append(new_element)
            j = j + 1
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))