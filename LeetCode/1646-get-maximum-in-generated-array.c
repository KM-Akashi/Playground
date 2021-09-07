int getMaximumGenerated(int n)
{
    if (n == 1 || n == 0)
        return n;
    int nums[n + 1];
    nums[0] = 0;
    nums[1] = 1;

    int max = -1;
    for (int i = 2; i < n + 1; i++)
    {
        nums[i] = nums[i / 2];
        if (i % 2)
            nums[i] += nums[i / 2 + 1];

        if (nums[i] > max)
            max = nums[i];
    }

    return max;
}