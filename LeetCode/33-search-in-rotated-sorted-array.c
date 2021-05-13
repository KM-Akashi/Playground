int search(int *nums, int numsSize, int target)
{
    int rotatedPos = 1;
    while (rotatedPos < numsSize && nums[rotatedPos - 1] < nums[rotatedPos])
        rotatedPos++;

    if (target < nums[0])
    {
        return BinarySearch(nums, rotatedPos, numsSize - 1, target);
    }
    else
    {
        return BinarySearch(nums, 0, rotatedPos - 1, target);
    }
}

int BinarySearch(int *vals, int left, int right, int key)
{
    int low = left;
    int high = right;
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