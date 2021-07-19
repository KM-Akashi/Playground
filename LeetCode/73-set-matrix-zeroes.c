void setZeroes(int **matrix, int matrixSize, int *matrixColSize)
{
    bool r = false, c = false;
    for (int i = 0; i < matrixSize; i++)
        if (matrix[i][0] == 0)
        {
            c = true;
            break;
        }
    for (int j = 0; j < *matrixColSize; j++)
        if (matrix[0][j] == 0)
        {
            r = true;
            break;
        }

    for (int i = 1; i < matrixSize; i++)
        for (int j = 1; j < *matrixColSize; j++)
            if (matrix[i][j] == 0)
            {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }

    for (int i = 1; i < matrixSize; i++)
        if (matrix[i][0] == 0)
            for (int j = 0; j < *matrixColSize; j++)
                matrix[i][j] = 0;
    for (int j = 1; j < *matrixColSize; j++)
        if (matrix[0][j] == 0)
            for (int i = 0; i < matrixSize; i++)
                matrix[i][j] = 0;

    if (c)
        for (int i = 0; i < matrixSize; i++)
            matrix[i][0] = 0;
    if (r)
        for (int j = 0; j < *matrixColSize; j++)
            matrix[0][j] = 0;
}