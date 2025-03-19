class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # edge case: grid is empty or grid is an empty list 
        if not grid or not grid[0]:
            return 0

        # get grid size
        m, n = len(grid), len(grid[0])
        numb_island = 0

        # define the recursive func dfs
        # call this dfs function when the position at grid is 1
        # check current position's neighbors
        # on the edges, out of bound, those are 0s
        # after visiting positions, convert 1 to 0
        def dfs(i, j):
            # think from the opposit way: when i, j out of bound or current position is 0
            # we return directly, without doing anything
            # this approach is more clear than thinking i in bound, j out of bound, etc  
            if i < 0 or i > m-1 or j < 0 or j > n-1 or grid[i][j]=='0':
                return 

            # i j in bound and this position is 1
            # flip 1 to 0 as visited
            grid[i][j] = '0'
            # iterate neighbors
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i+1, j)
            dfs(i, j-1)

        # iterate all position index on rows and columns 
        # when the position is 1, call dfs function 
        # once it is a 1, island counter + 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    numb_island += 1
                    dfs(i, j)
        
        return numb_island
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # =============old thoughts===========================
        # island is a group of '1's around by '0's
        # overall approach
        # find the first 1, then go up, left, down and right to see if they are 1s
        # figure out all 1s in this group, 
        # challenge: how to know two islands are separate? or are they connected as one big island?
        # explore your neighbors until there is no new 1s, which means this is a group of 1s for an island
        # then, a global index may move to next un-discovered position 
        # if water, continue
        # if land, try find its neighbors are 1 or 0
        # until discover all 

        # need a map to indicate the un-discovered position
        # it is ok to use either DFS or BFS
        # discover_map = grid
        # numb_island = 0

        # challenge: should I build a node with up, left, down and right? 

