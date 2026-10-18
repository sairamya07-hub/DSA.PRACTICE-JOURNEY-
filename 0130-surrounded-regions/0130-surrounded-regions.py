class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs (i,j,vis,grid,n,m):
            for r ,c in [[-1,0],[1,0],[0,-1],[0,1]]:
                nr=r+i
                nc=c+j
                if(nr>=0 and nr<n and nc>=0 and  nc<m and grid[nr][nc]=="O" and vis[nr][nc]==0):
                    vis[nr][nc]=1
                    dfs(nr,nc, vis,grid,n,m)

        n=len(grid)
        m=len(grid[0])
        vis=[]
        for i in range (n):
            lst=[0]*m
            vis.append(lst)

        for i in range (n):
            for j in range (m):
                # FIXED THIS CONDITION ONLY
                if ((i==0 or i==n-1 or j==0 or j==m-1 ) and grid[i][j]=="O" and vis[i][j]==0):
                    vis[i][j]=1
                    dfs(i,j,vis,grid,n,m)

        for i in range(n):
            for j in range (m):
                if (grid[i][j]=="O" and vis[i][j]==0):
                    grid[i][j]="X"

        return grid

        