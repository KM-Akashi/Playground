void sortColors(int *nums, int numsSize)
{
    int colorCount[3] = {0, 0, 0};
    for (int i = 0; i < numsSize; i++)
        colorCount[nums[i]] += 1;

    for (int i = 0; i < colorCount[0]; i++)
        nums[i] = 0;
    for (int i = 0; i < colorCount[1]; i++)
        nums[colorCount[0] + i] = 1;
    for (int i = 0; i < colorCount[2]; i++)
        nums[colorCount[0] + colorCount[1] + i] = 2;
}