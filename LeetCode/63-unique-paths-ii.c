#include <stdbool.h>

int uniquePathsWithObstacles(int **obstacleGrid, int obstacleGridSize, int *obstacleGridColSize)
{
    int m = obstacleGridSize;
    int n = *obstacleGridColSize;

    int count[m][n];

    int flag = false;
    for (int i = 0; i < m; i++)
    {
        if (obstacleGrid[i][0])
            flag = true;
        if (flag)
            count[i][0] = 0;
        else
            count[i][0] = 1;
    }
    flag = false;
    for (int i = 0; i < n; i++)
    {
        if (obstacleGrid[0][i])
            flag = true;
        if (flag)
            count[0][i] = 0;
        else
            count[0][i] = 1;
    }

    for (int i = 1; i < m; i++)
        for (int j = 1; j < n; j++)
        {
            if (obstacleGrid[i][j])
                count[i][j] = 0;
            else
                count[i][j] = count[i - 1][j] + count[i][j - 1];
        }

    return count[m - 1][n - 1];
}