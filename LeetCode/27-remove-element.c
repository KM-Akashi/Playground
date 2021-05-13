int removeElement(int *nums, int numsSize, int val)
{
    int left = 0, right = 0;
    while (right < numsSize)
    {
        if (nums[right] != val)
            nums[left++] = nums[right++];
        else
            right++;
    }
    return left;
}