int min(int a, int b)
{
    if (a < b)
        return a;
    else
        return b;
}

int minPathSum(int **grid, int gridSize, int *gridColSize)
{
    int m = gridSize;
    int n = *gridColSize;
    int count[m][n];

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i == 0 && j == 0)
            {
                count[i][j] = grid[i][j];
                continue;
            }

            int fromTop, fromLeft;
            if (i == 0)
                fromTop = 1000;
            else
                fromTop = count[i - 1][j];
            if (j == 0)
                fromLeft = 1000;
            else
                fromLeft = count[i][j - 1];

            count[i][j] = min(fromTop, fromLeft) + grid[i][j];
        }
    }
    return count[m - 1][n - 1];
}