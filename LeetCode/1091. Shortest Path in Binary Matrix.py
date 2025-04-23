from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # find the shortest path from top left to bottom right 
        #   if no path, then return -1
        # potentil solution: 
        #   recursive bfs 
        # corner cases: 
        #   - 1 cell only
        #   - cell on the edge: so accessable directions are limited on inner sides

        # first, how to convert this list in list grid to a map?
        # maybe no need to convert, but iterate the list with index i and j for row and column 
        # any visited place can be labelled as 1 from 0

        n = len(grid)
        # 1. check if starting and ending position are blocked
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        
        # 2. initialize dequeue (BFS)
        queue = deque()
        queue.append((0, 0, 1))
        
        # 3. directions of move in 8 directions (row_idx, col_idx)
        directions = [(-1, -1), (-1, 0), (-1,1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]
        
        # 4. BFS
        while queue:
            row, col, dist = queue.popleft()

            # reach right bottom corner and stop?
            if row == n-1 and col == n-1:
                return dist 

            # check 8 directions
            for dr, dc in directions:
                r = row + dr
                c = col + dc

                # only within the valid range and not visited 
                if 0 <= r < n and 0 <= c < n and grid[r][c] == 0:
                    queue.append((r, c, dist+1)) # push a potential cell to queue
                    grid[r][c] = 1 # label it as visited
                
        return -1 # until now, code does not return at row and col equal to n-1, no path found then
                