/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *countBits(int num, int *returnSize)
{
    int *count = (int *)malloc(sizeof(int) * (num + 1));
    count[0] = 0;
    for (int i = 1; i < num + 1; i++)
    {
        int lastBit = i - ((i >> 1) << 1);
        count[i] = lastBit + count[i >> 1];
    }
    *returnSize = num + 1;
    return count;
}