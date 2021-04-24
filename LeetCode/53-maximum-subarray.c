int maxSubArray(int *nums, int numsSize)
{
    if (numsSize == 1)
        return nums[0];
    int max_sum[numsSize];
    for (int i = 0; i < numsSize; i++)
    {
        if (i == 0)
            max_sum[i] = nums[i];
        else
        {
            if (max_sum[i - 1] > 0)
                max_sum[i] = nums[i] + max_sum[i - 1];
            else
                max_sum[i] = nums[i];
        }
    }
    int max = max_sum[0];
    for (int i = 0; i < numsSize; i++)
        if (max < max_sum[i])
            max = max_sum[i];
    return max;
}