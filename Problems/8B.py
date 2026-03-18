from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        r, c = len(grid), len(grid[0])
        cnt = 0
        brCol = c
        
        # Create prefix sum array
        prefix = [[0] * c for _ in range(r)]
        
        # First cell
        prefix[0][0] = grid[0][0]
        if prefix[0][0] > k:
            return 0
        cnt += 1
        
        # First row
        for j in range(1, c):
            prefix[0][j] = prefix[0][j-1] + grid[0][j]
            if prefix[0][j] > k:
                brCol = j
                break
            cnt += 1
        
        # Remaining rows
        for i in range(1, r):
            prefix[i][0] = prefix[i-1][0] + grid[i][0]
            if prefix[i][0] > k:
                break
            cnt += 1
            
            for j in range(1, brCol):
                prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + grid[i][j]
                
                if prefix[i][j] > k:
                    brCol = j
                    break
                cnt += 1
        
        return cnt

