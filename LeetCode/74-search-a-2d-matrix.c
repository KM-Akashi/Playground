int BinarySearch(int *vals, int size, int key)
{
    int low = 0;
    int high = size - 1;
    while (low <= high)
    {
        int mid = (int)((low + high) / 2);
        if (vals[mid] == key)
            return mid;
        else if (key < vals[mid])
            high = mid - 1;
        else
            low = mid + 1;
    }

    return -1;
}

bool searchMatrix(int **matrix, int matrixSize, int *matrixColSize, int target)
{
    for (int r = 0; r < matrixSize; r++)
    {
        if (matrix[r][0] == target || matrix[r][*matrixColSize - 1] == target)
            return true;
        if (matrix[r][0] < target && matrix[r][*matrixColSize - 1] > target)
            if (BinarySearch(matrix[r], *matrixColSize, target) != -1)
                return true;
    }
    return false;
}