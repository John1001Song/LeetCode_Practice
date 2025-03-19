        # we need to recursively check node by node 
        # use a set to contain visited nodes
        # once current node is visited
        # input this node, output the copy of this node 

        # dict stores visited nodes
        visited = dict()

        # edge case empty graph
        # how to check adjList
        if node == None:
            return None
        
        # edge case one node without neighbors
        # if node == Node(1, None):
        #     return [[]]
        
        def checkNode(cur_node):
            if cur_node.val in visited:
                return visited[cur_node.val]
            else: 
                # create a copy of this node 
                copy_node = Node(cur_node.val, None)
                visited[cur_node.val] = copy_node
                for neignbor in cur_node.neighbors:
                    copy_node.neighbors.append(checkNode(neignbor))

            return copy_node

        # convert this output dict to list 

        return checkNode(node)