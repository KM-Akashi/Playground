int removeDuplicates(int *nums, int numsSize)
{
    if (numsSize == 0 || numsSize == 1)
        return numsSize;
    int numsSizeAfterRemove = 1;
    int a, b;
    a = 0;
    b = 1;
    while (b < numsSize)
    {
        while (b < numsSize && nums[b] == nums[a])
            b++;
        if (b < numsSize && nums[b] != nums[a])
        {
            numsSizeAfterRemove++;
            a++;
            nums[a] = nums[b];
        }
    }
    int numsRemove[numsSizeAfterRemove];
    for (int i = 0; i < numsSizeAfterRemove; i++)
    {
        numsRemove[i] = nums[i];
    }
    return numsSizeAfterRemove;
}